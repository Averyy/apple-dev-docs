# Evaluating a Core AI model

**Framework**: Evaluations

Bundle a model with your app and measure how well the model classifies sentiment compared to the default on-device model.

**Availability**:
- macOS 27.0+
- Xcode 27.0+

#### Overview

The Foundation Models framework supports running a model in several places: on device, on Apple’s Private Cloud Compute, or on a server to which you connect. You can also bundle a model directly in your app, which you pick based on its size, license, or capability. [`Core AI`](https://developer.apple.com/documentation/coreai) makes this option possible by running the model on Apple silicon. Use the open source [`coreai-models`](https://developer.apple.comhttps://github.com/apple/coreai-models) Swift package to convert a model into Core AI format; the Core AI runtime then loads and runs it on device. This sample code project exports one such model, runs it through a [`LanguageModelSession`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession), and measures its quality with the Evaluations framework. For how to export a model and run it in a session, see [`Running a Core AI model in a Foundation Models session`](https://developer.apple.com/documentation/foundationmodels/running-a-core-ai-model-in-a-foundation-models-session).

The model under test in this sample project is a small quantized model suitable for running on device. The sample project exports it to the Core AI format and loads it through the `coreai-models` provided `CoreAILanguageModel`. This type conforms to [`LanguageModel`](https://developer.apple.com/documentation/foundationmodels/languagemodel), so the session, prompts, and instructions are the same whether the app uses the bundled model or the system’s built-in one; only the model changes. The sample project evaluates the Core AI model on a three-way sentiment-classification problem, labeling each input as negative, neutral, or positive. It then runs the same evaluation against the system’s on-device default model, so you can compare the two side by side.

![A screenshot of the Compare Evaluations report in Xcode, with the Core AI model in the left column and the on-device default in the right column. The top of the report lists aggregated metrics such as mean accuracy, recall, and precision for each model, and the table below shows per-prompt pass and fail results.](/images/com.apple.evaluations/default-vs-coreai-detail@2x.png)

#### Configure the Sample Code Project

Run this sample project on macOS 27 or later with Xcode 27 or later. Before you run it, export the model and prepare Xcode:

1. Install the `uv` package manager and `git` if they aren’t already present.
2. From the project directory, run the helper script to export the model into `Models/coreai-model`: ```bash
./scripts/prepare-model.sh
``` The first run downloads the model and exports it for macOS, which takes several minutes. The project excludes the export from source control because of its size.
3. In Xcode, choose Xcode > Settings > Components, and install the Metal Toolchain. Building a target that contains a Core AI model requires it. For more information on configuring a project with an `.aimodel` file, see [`Integrating on-device AI models in your app with Core AI`](https://developer.apple.com/documentation/coreai/integrating-on-device-ai-models-in-your-app-with-core-ai).
4. Confirm that the CoreAIEvals app target includes the exported model folder as a folder reference, so Xcode copies it into the app bundle.

#### Load the Core Ai Model

The sample project loads the exported model using `CoreAILanguageModel`, passing the URL of the bundled resource folder. Loading is asynchronous; before the first request, Core AI compiles the model and loads its tokenizer. To avoid repeating that work for every prompt, a `CoreAIModelStore` actor loads the model once and caches it. It’s an actor so the model is only loaded once even if there are concurrent calls:

```swift
import CoreAILanguageModels

actor CoreAIModelStore {
    static let shared = CoreAIModelStore()

    private static let modelResourceName = "coreai-model"
    private var cached: CoreAILanguageModel?

    func model() async throws -> CoreAILanguageModel {
        if let cached { return cached }

        guard let url = Bundle.main.url(forResource: Self.modelResourceName, withExtension: nil) else {
            throw CoreAIModelStoreError.modelNotBundled(resourceName: Self.modelResourceName)
        }

        let model = try await CoreAILanguageModel(resourcesAt: url)
        cached = model
        return model
    }
}
```

#### Classify Text in a Model Session

This sample project performs a *sentiment classification* that sorts each piece of text into one of a fixed set of labels, which in this case is negative, neutral, or positive. Classification like this is a common language task, useful for triaging reviews, feedback, or support messages, and it’s a natural fit for evaluation because every input has a known correct label to score the model against.

In the sample project, every classification runs through one shared path that creates a [`LanguageModelSession`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession) and returns a guided-generation result: a `SentimentVerdict`. The [`Generable`](https://developer.apple.com/documentation/foundationmodels/generable) macro defines the shape of that result:

```swift
@Generable
enum Sentiment: String, Codable {
    case negative
    case neutral
    case positive
}

@Generable
struct SentimentVerdict: Codable, Equatable {
    @Guide(description: "One short sentence explaining why this sentiment was chosen.")
    let reasoning: String
    @Guide(description: "How confident you are in the sentiment choice.", .range(0...100))
    let confidence: Int
    @Guide(description: "The overall sentiment: negative, neutral, or positive.")
    let sentiment: Sentiment
}
```

The Core AI model and the on-device default differ only in the model the session receives; the instructions and the generated output type are identical. A `ClassifierBackend` value names which model to use.

```swift
enum ClassifierBackend {
    case coreAI
    case onDeviceDefault

    /// A human-readable name for menus, labels, and evaluation reports.
    nonisolated var displayName: String {
        switch self {
        case .coreAI: "Core AI model"
        case .onDeviceDefault: "Default on-device model"
        }
    }
}
```

A `SentimentClassifier` turns a prompt into a `SentimentVerdict`, and both the app and the evaluation share this one classification path. It’s an enum of static members: `classify(_:using:)` builds the session, sends the prompt, and returns the generated verdict, while a private `makeSession(for:)` supplies the right model and the shared instructions:

```swift
enum SentimentClassifier {
    /// The classification instructions, passed into the LanguageModelSession.
    private static let instructions = """
        You classify the sentiment of the user's text as exactly one of: \
        negative, neutral, or positive.

        Text that only states facts — describing features, specs, logistics, \
        schedules, or events with no opinion — is NEUTRAL, even when it sounds \
        pleasant or reports something working. Absence of any complaint does not \
        make text positive.

        - positive: clear approval, satisfaction, or praise.
        - negative: clear disapproval, dissatisfaction, or criticism.
        - neutral: factual/no opinion, OR only mild, lukewarm evaluation \
        ("fine", "okay", "average", "does what it says").

        If the text mixes positive and negative points, pick the side that \
        dominates; if neither dominates, it is neutral.

        Always fill in reasoning, confidence and sentiment. Keep reasoning to one \
        short sentence. For confidence (0–100), use the full range: 80–100 only \
        when the sentiment is unambiguous, lower when borderline.
        """

    /// Builds a fresh `LanguageModelSession` backed by `backend`.
    private static func makeSession(for backend: ClassifierBackend) async throws -> LanguageModelSession {
        switch backend {
        case .coreAI:
            let coreAIModel = try await CoreAIModelStore.shared.model()
            return LanguageModelSession(model: coreAIModel, instructions: instructions)
        case .onDeviceDefault:
            return LanguageModelSession(model: .default, instructions: instructions)
        }
    }

    static func classify(
        _ prompt: Prompt,
        using backend: ClassifierBackend
    ) async throws -> SentimentVerdict {
        let session = try await makeSession(for: backend)
        let response = try await session.respond(to: prompt, generating: SentimentVerdict.self)
        return response.content
    }
}
```

The instructions define what each label means and how to resolve the hard cases, such as factual text that reads as pleasant and mixed sentiment.

#### Evaluate the Model

The sample project’s single `SentimentClassificationEvaluation` type conforms to [`Evaluation`](evaluation.md). It runs the same `SentimentClassifier` classification path the app uses: its [`subject(from:)`](evaluation/subject(from:).md) method calls `SentimentClassifier.classify` and returns a [`ModelSubject`](modelsubject.md) that wraps the model’s verdict for the framework to score. Its `backend` property holds the model to test, so the same dataset, metrics, and aggregations score both models:

```swift
struct SentimentClassificationEvaluation: Evaluation {
    let backend: ClassifierBackend

    var name: String { backend.displayName }
    let dataset = SentimentDataset.all

    func subject(from sample: ModelSample<SentimentVerdict>) async throws -> ModelSubject<SentimentVerdict> {
        ModelSubject(value: try await SentimentClassifier.classify(sample.prompt, using: backend))
    }
}
```

That `dataset` is 60 labeled prompts, 20 for each sentiment. It deliberately mixes clear-cut cases with harder ones, such as faint praise, sarcasm, and complaints framed as neutral-sounding facts, so the metrics measure more than the easy wins. Each entry is a [`ModelSample`](modelsample.md) that pairs a prompt with the expected `SentimentVerdict`:

```swift
enum SentimentDataset {
    static let all = ArrayLoader<ModelSample<SentimentVerdict>>(samples: [
        ModelSample(prompt: "Absolutely loved this — best purchase I've made all year. Works flawlessly.",
            expected: SentimentVerdict(reasoning: "Expresses strong satisfaction and praise.",
                confidence: 100, sentiment: .positive)),
        ModelSample(prompt: "Looks nice, but it stopped working after a week.",
            expected: SentimentVerdict(reasoning: "Brief positive overridden by a failure complaint.",
                confidence: 85, sentiment: .negative)),
        // ... 58 more, balanced across positive, negative, and neutral.
    ])
}
```

#### Score Accuracy Precision and Recall

The same `SentimentClassificationEvaluation` type declares the [`Metric`](metric.md) values it tracks. Alongside overall accuracy, it scores precision and recall for each sentiment class. It also scores the model’s self-reported confidence, both overall and split by whether the prediction was right:

```swift
let accuracy = Metric("Accuracy")

let positiveRecall = Metric("Recall (positive)")
let negativeRecall = Metric("Recall (negative)")
let neutralRecall  = Metric("Recall (neutral)")

let positivePrecision = Metric("Precision (positive)")
let negativePrecision = Metric("Precision (negative)")
let neutralPrecision  = Metric("Precision (neutral)")

let confidence            = Metric("Confidence")
let confidenceWhenCorrect = Metric("Confidence (when correct)")
let confidenceWhenWrong   = Metric("Confidence (when wrong)")
```

Each [`Evaluator`](evaluator.md) scores one data sample against one metric. Precision and recall share the same pass-or-fail pattern. Both use [`ignore(rationale:)`](metric/ignore(rationale:).md) to drop data samples that don’t belong to the class under measurement. The recall evaluator for a class ignores every data sample not labeled with that class. It then passes when the prediction matches, and fails when it doesn’t:

```swift
func recallEvaluator(for target: Sentiment, metric: Metric) -> Evaluator<ModelSample<SentimentVerdict>> {
    Evaluator { input, subject in
        guard input.expected?.sentiment == target else { return metric.ignore() }
        return subject.value.sentiment == target
            ? metric.passing(rationale: "caught \(target.rawValue)")
            : metric.failing(rationale: "missed \(target.rawValue), predicted \(subject.value.sentiment.rawValue)")
    }
}
```

Precision mirrors this approach, ignoring every data sample not predicted as the class. The [`evaluators`](evaluation/evaluators-swift.property.md) property lists one recall and one precision evaluator per class.

Each evaluator passes a rationale to [`passing(rationale:)`](metric/passing(rationale:).md) or [`failing(rationale:)`](metric/failing(rationale:).md). The report displays that rationale in the drill-down for a single data sample, so each result explains itself. In the example below, the dataset labels “Looks nice, but it stopped working after a week.” as negative. Because the Core AI model predicts neutral instead, the sample fails accuracy, negative recall, and neutral precision, each with its rationale. The table beneath compares the verdict field by field: the predicted sentiment, confidence, and reasoning all differ from the expected values, which the report flags:

![A screenshot of the Core AI model run in Xcode’s evaluation report, with the per-prompt list on the left and the drill-down for the selected data sample on the right. A row of cards shows Accuracy, Recall (negative), and Precision (neutral) all failing, alongside a Confidence of 0.80 and a Confidence (when wrong) of 0.80. A table below lists the model’s value, the expected value, and any issue found for each field: the confidence of 80 falls short of the expected 85, the reasoning differs from the expected summary, and the predicted sentiment of neutral doesn’t match the expected negative.](/images/com.apple.evaluations/coreai-drill-down@2x.png)

The [`aggregateMetrics(using:)`](evaluation/aggregatemetrics(using:).md) method reduces the per-sample results into the summary. The mean of a pass-or-fail metric is a rate, so the mean of `accuracy` is the overall accuracy. Grouping keeps the per-class figures together:

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.computeMean(of: accuracy)

    aggregator.group("Recall") { group in
        group.computeMean(of: positiveRecall)
        group.computeMean(of: negativeRecall)
        group.computeMean(of: neutralRecall)
    }
    aggregator.group("Precision") { group in
        group.computeMean(of: positivePrecision)
        group.computeMean(of: negativePrecision)
        group.computeMean(of: neutralPrecision)
    }
}
```

Each grouped metric becomes a card in the report for a single run. Here the Core AI model’s run shows each metric’s aggregated value as a pass-to-fail bar for precision, recall, and accuracy:

![A screenshot of the evaluation report for a single run, the Core AI model, in Xcode. Grouped cards show the precision, recall, and accuracy metrics the evaluation declares. Each card shows an aggregated value above a pass-to-fail bar.](/images/com.apple.evaluations/coreai-stats@2x.png)

#### Compare Against the on Device Default

The `SentimentClassificationEvaluationTests` suite creates one evaluation for the Core AI model and another for the on-device default. The on-device default provides the baseline for the comparison report below. The `name` in each `info` dictionary labels the run in the report using the model’s `displayName`.

```swift
struct SentimentClassificationEvaluationTests {
    static let coreAIEvaluation = SentimentClassificationEvaluation(backend: .coreAI)

    @Test(.evaluates(Self.coreAIEvaluation, info: ["name": ClassifierBackend.coreAI.displayName]))
    func testCoreAISentimentClassification() async throws {
        let context = EvaluationContext.current
        print(context.result.groupedSummary)
    }

    static let defaultOnDeviceModelEvaluation = SentimentClassificationEvaluation(backend: .onDeviceDefault)

    @Test(.evaluates(Self.defaultOnDeviceModelEvaluation, info: ["name": ClassifierBackend.onDeviceDefault.displayName]))
    func testDefaultSentimentClassification() async throws {
        let context = EvaluationContext.current
        print(context.result.groupedSummary)
    }
}
```

Run both tests the usual way: choose Product > Test, or click the diamond in the gutter next to each `@Test` function. When a run finishes, open the Report navigator and select its Evaluations item to see the results.

Both evaluations share one dataset and one set of metrics, so confidence, accuracy, recall, and precision are directly comparable. Xcode lists the two runs together in the Report navigator. The Compare Evaluations report shows their metrics side by side:

![A screenshot of the evaluation report navigator in Xcode comparing two runs as rows, the Core AI model above the on-device default. Columns show recall, precision, and accuracy ratios for each run, with the on-device default scoring the higher accuracy of the two.](/images/com.apple.evaluations/default-vs-coreai-summary@2x.png)

In this comparison the on-device default has the higher accuracy, although a different model might produce a better score. Accuracy is only one factor, alongside size, license, and capability, and an evaluation like this gives you the numbers to weigh them and choose the right model for your app.

## See Also

- [Evaluating language model responses](evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Designing effective evaluations](designing-effective-evaluations.md)
  Design evaluations that tell you how well your feature works, why it fails, and where to focus next.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md)
  Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.
- [protocol Evaluation](evaluation.md)
  A type that defines an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluating-a-core-ai-model)*