# Evaluating multimodal prompts

**Framework**: Evaluations  
**Role**: Sample Code  
**Download**: [EvaluatingMultimodalPrompts.zip](https://docs-assets.developer.apple.com/published/c55b9999bd15/EvaluatingMultimodalPrompts.zip)

Measure how well an on-device model classifies food photos, using a multimodal prompt and a streamed image dataset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- Xcode 27.0+

## Overview

A prompt is the input you give a model to guide its response. With the Foundation Models framework, a prompt can be multimodal: you add an image to a [`Prompt`](../FoundationModels/prompt.md) alongside your text, and the model reasons about the image and the text together. This sample code project is a macOS and iOS app named Grub Gander that:

- Sends a food photo and a question to an on-device [`LanguageModelSession`](../FoundationModels/languagemodelsession.md) in one prompt.
- Classifies the food as healthy, unhealthy, or not food at all.
- Measures how well the model does in a separate evaluation.

You run that evaluation as a test, using the Evaluations framework and a labeled image dataset. The scores cover overall accuracy, per-class precision and recall, and confidence calibration.

![A screenshot of the Grub Gander app after it classifies a photo. A photo of apples fills most of the window, with a verdict banner reading HEALTHY over it. Text at the bottom of the photo reads 95% confident and explains that the apples are whole, minimally processed fruit. A row of selectable sample thumbnails runs along the bottom of the window.](https://developer.apple.com/tutorials/images/com.apple.evaluations/classify-result@2x.png)

Image evaluation has a problem that text evaluation doesn’t: a decoded photo can use a large amount of memory. The built-in [`ArrayLoader`](./arrayloader.md) holds an entire dataset in memory at once, which is fine for text but doesn’t scale to thousands of images. To avoid that, this project streams its dataset from disk instead.

## Configure the sample code project

The app and its evaluation use the on-device model designed for Apple Intelligence. Run the app on macOS 27 or later, or on a physical iOS 27 device. Use Xcode 27 or later.

The evaluation dataset is large, so it isn’t included in the sample project. Prepare it before you run the tests:

1. Install the `uv` package manager if it isn’t already present.
2. From the `GrubGander/` directory, download the dataset into the test data folder:

   ```bash
   uv run Tools/prepare_dataset.py --out GrubGander/EvalData --per-class 100
   ```

   This download process writes an image-folder layout and an `eval.jsonl` manifest into `GrubGander/EvalData`.
3. Run the tests with Product > Test. The evaluation reads `EvalData` in place from the source tree, so there’s no resource-copy step to rebuild.

## Build a multimodal prompt

The classifier returns a guided-generation result named `FoodVerdict`. The [`Generable`](../FoundationModels/generable.md) macro defines its shape, and its category is a `FoodCategory`. The project declares `reasoning` before `category` on purpose: the model fills the fields in order, so it commits to an explanation before it picks an answer:

```swift
@Generable
enum FoodCategory: String, Equatable, Sendable, Codable, CaseIterable {
    case healthy
    case unhealthy
    case notFood = "not_food"
}

@Generable
struct FoodVerdict: Equatable, Sendable, Codable {
    @Guide(description: "A brief, specific explanation of why the image belongs to the chosen category.")
    let reasoning: String
    @Guide(description: "The single best category for the image")
    let category: FoodCategory
    @Guide(description: "How confident you are that the answer is correct.", .range(0...100))
    let confidence: Int
}
```

The `FoodClassifier.prompt(for:)` method builds a [`Prompt`](../FoundationModels/prompt.md) that pairs an image `Attachment` with the question text. Both the app and the evaluations call this method, so the prompt they send can’t drift apart:

```swift
nonisolated static let question = "What category best describes this image?"

/// Take an image and convert it to a prompt.
nonisolated static func prompt(for image: CGImage) -> Prompt {
    Prompt {
        Attachment(image)
        question
    }
}
```

Classifying an image-and-text prompt is no different from classifying a text prompt: the attached image is just another part of the prompt, and the instructions define the task. Two `classify(_:)` overloads run it: one takes a `CGImage` and builds the prompt; the other takes a prepared `Prompt`, opens a session, and returns the verdict:

```swift
nonisolated static let instructions = """
    You are a careful food-image classifier. Decide whether an image shows \
    healthy food, unhealthy food, or something that isn't food at all. \
    "Healthy" is whole or minimally processed food — fruits, vegetables, \
    nuts, grains. "Unhealthy" is sugary, fried, or heavily processed food — \
    desserts, candy, pastries.
    """

/// Classify an image on the on-device system model.
nonisolated static func classify(_ image: CGImage) async throws -> FoodVerdict {
    try await classify(prompt(for: image))
}

/// Classify a prepared prompt on the on-device system model.
nonisolated static func classify(_ prompt: Prompt) async throws -> FoodVerdict {
    let session = LanguageModelSession(instructions: instructions)
    return try await session.respond(to: prompt, generating: FoodVerdict.self).content
}
```

## Stream the dataset one image at a time

A [`Loader`](./loader.md) supplies an evaluation’s samples. Instead of the built-in [`ArrayLoader`](./arrayloader.md), this project uses a `JSONLImageSampleLoader`. The loader:

- Streams the dataset from disk.
- Decodes each image only when the evaluation asks for it.
- Keeps peak memory close to a single image.

This custom loader conforms to [`Loader`](./loader.md) and returns an `AsyncSequence` that produces samples lazily. Its `stream` reads a JSON Lines manifest one line at a time:

```swift
struct JSONLImageSampleLoader: Loader {
    typealias Sample = ModelSample<FoodVerdict>

    let directory: URL
    var maxPixelSize: Int = 1536

    private struct Record: Decodable {
        let image: String
        let label: String
    }

    var stream: any AsyncSequence<ModelSample<FoodVerdict>, any Error> {
        // Capture the loader's values so the producing task doesn't retain `self`.
        let manifestURL = directory.appending(path: "eval.jsonl")
        let imageRoot = directory
        let maxPixelSize = maxPixelSize

        return AsyncThrowingStream(ModelSample<FoodVerdict>.self) { continuation in
            // A missing dataset yields an empty run rather than an error; callers
            // gate on `EvalDataset.isAvailable` and skip the eval before reaching here.
            guard FileManager.default.fileExists(atPath: manifestURL.path) else {
                continuation.finish()
                return
            }
            let task = Task {
                do {
                    let handle = try FileHandle(forReadingFrom: manifestURL)
                    defer { try? handle.close() }
                    let decoder = JSONDecoder()

                    // `.lines` streams the file lazily; it does not read it all up front.
                    for try await line in handle.bytes.lines {
                        try Task.checkCancellation()
                        let trimmed = line.trimmingCharacters(in: .whitespaces)
                        guard !trimmed.isEmpty else { continue }

                        let record = try decoder.decode(Record.self, from: Data(trimmed.utf8))
                        guard let category = FoodCategory.fromDatasetLabel(record.label) else {
                            continue   // An unrecognized label, so skip rather than crash the run.
                        }
                        let imageURL = URL(fileURLWithPath: record.image, relativeTo: imageRoot)
                        guard let image = Self.decodeImage(at: imageURL, maxPixelSize: maxPixelSize) else {
                            continue   // A missing or corrupt image, so skip it.
                        }

                        continuation.yield(
                            ModelSample(
                                prompt: FoodClassifier.prompt(for: image),
                                expected: FoodVerdict(reasoning: "", category: category, confidence: 50),
                                instructions: Instructions(FoodClassifier.instructions)
                            )
                        )
                    }
                    continuation.finish()
                } catch {
                    continuation.finish(throwing: error)
                }
            }
            continuation.onTermination = { _ in task.cancel() }
        }
    }
}
```

Two details keep peak memory to about one image:

- `FileHandle.bytes.lines` reads the manifest lazily, so the whole file is never held in memory.
- Each decoded `CGImage` lives only inside its sample’s [`prompt`](./modelsample/prompt.md). Once the harness finishes that sample and moves to the next, nothing references the image, and the system frees it.

Decoding uses ImageIO’s thumbnail path with a `maxPixelSize` cap, which downscales the image and applies its EXIF orientation without ever creating the full-resolution bitmap. The on-device model doesn’t need full-resolution photos.

Each manifest line names an image and its *ground-truth* label, the answer that’s been verified as correct. The loader resolves the image paths against its `directory`:

```swift
{"image": "images/test/healthy/000123.jpg", "label": "healthy"}
{"image": "images/test/not_food/004501.jpg", "label": "not_food"}
```

Only `category` has a ground-truth label; the expected `reasoning` is empty, and the expected `confidence` is a neutral 50.

## Evaluate the classifier

The `FoodEvaluation` type conforms to [`Evaluation`](./evaluation.md). Its `dataset` is a `JSONLImageSampleLoader` that points at the prepared `EvalData` folder, and its [`subject(from:)`](./evaluation/subject%28from%29.md) method routes each sample through the same `FoodClassifier.classify(_:)` call the app uses, so the evaluation measures exactly what ships:

```swift
struct FoodEvaluation: Evaluation {
    let name = "Food Classification"

    var dataset: JSONLImageSampleLoader {
        JSONLImageSampleLoader(directory: EvalDataset.directory)
    }

    func subject(from sample: ModelSample<FoodVerdict>) async throws -> ModelSubject<FoodVerdict> {
        // Route through the exact call the app makes, so the eval measures what ships.
        let verdict = try await FoodClassifier.classify(sample.input.prompt)
        return ModelSubject(value: verdict)
    }
}
```

The evaluation declares several [`Metric`](./metric.md) values: one for overall accuracy; for each of the three ground-truth classes, a precision metric (the share of a class’s predictions that are correct) and a recall metric (the share of a class’s samples the model finds); and three more that track confidence overall, on correct predictions, and on wrong ones. Each [`Evaluator`](./evaluator.md) scores one sample against one metric, calling [`ignore(rationale:)`](./metric/ignore%28rationale%29.md) to drop samples outside the class it measures:

- A recall evaluator ignores every sample whose true label isn’t its class.
- A precision evaluator ignores every sample the model didn’t predict as its class.

The `recall(_:forClass:)` helper builds one such evaluator:

```swift
private func recall(_ metric: Metric, forClass category: FoodCategory)
    -> Evaluator<ModelSample<FoodVerdict>> {
    Evaluator { input, subject in
        guard input.expected?.category == category else { return metric.ignore() }
        return subject.value.category == category ? metric.passing() : metric.failing()
    }
}
```

The confidence evaluators work differently from the precision and recall evaluators. They emit a continuous value with [`scoring(_:rationale:)`](./metric/scoring%28_,rationale%29.md) instead of a pass or fail, and they split confidence by whether the prediction was correct. Self-reported confidence is uncalibrated, so the signal worth watching is whether confidence drops on wrong answers.

The [`aggregateMetrics(using:)`](./evaluation/aggregatemetrics%28using%29.md) method reduces the per-sample results into grouped summaries: the mean of the pass-or-fail accuracy metric gives the overall accuracy rate, and grouping keeps the per-class figures together. The test then prints the summary and computes a macro-averaged F1 across the three classes — a single score that combines each class’s precision and recall, and stays high only when both are high. Macro-averaging takes the plain mean of the three classes’ F1 scores, so each class counts equally regardless of how many samples it has. Finally, the test asserts conservative regression floors so a bad model fails:

```swift
@Test(
    .enabled(if: SystemLanguageModel.default.availability == .available && EvalDataset.isAvailable),
    .evaluates(Self.evaluation)
)
func runFoodClassification() async throws {
    let result = EvaluationContext.current.result
    print(result.groupedSummary)

    let macroF1 = Self.evaluation.macroF1(from: result)
    // Conservative regression floors so the eval can actually fail on a bad model.
    #expect(result.aggregateValue(.mean(of: Self.evaluation.correct)) >= 0.55)
    #expect(macroF1 >= 0.45)
}
```

The `enabled(if:)` trait checks two things: the model’s availability and the dataset’s presence. The evaluation is skipped when either one is missing.

![A screenshot of the evaluation’s grouped summary in the Xcode test report. The metrics are grouped into Overall accuracy, Per-Class Precision and Per-Class Recall for the healthy, unhealthy, and not-food classes, and Confidence. Each precision and recall metric shows a pass ratio with a pass-fail bar. The confidence group shows average scores split by correct and incorrect predictions, along with a standard deviation.](https://developer.apple.com/tutorials/images/com.apple.evaluations/evaluation-summary@2x.png)

## See Also

### Essentials
- [Evaluating language model responses](./evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Designing effective evaluations](./designing-effective-evaluations.md)
  Design evaluations that tell you how well your feature works, why it fails, and where to focus next.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](./book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md)
  Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.
- [Evaluating a Core AI model](./evaluating-a-core-ai-model.md)
  Bundle a model with your app and measure how well the model classifies sentiment compared to the default on-device model.
- [protocol Evaluation](./evaluation.md)
  A type that defines an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluating-multimodal-prompts)*