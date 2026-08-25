# Generating synthetic datasets

**Framework**: Evaluations

Expand a small set of manually written evaluation samples into a larger dataset.

#### Overview

When you create evaluation samples manually, you get tight control over quality, but the process is time-consuming. Use a model to synthetically produce a much larger dataset from a small initial set, which gives you broader coverage for testing consistency and quality across inputs.

Each [`ModelSample`](modelsample.md) pairs a prompt the model receives with an optional expected output you evaluate against.

The framework adds a `makeSamples(_:targetCount:sessionProvider:validator:)` method to any array of `ModelSample` values. Call this method with a prompt that describes what to generate, and it returns new samples as an asynchronous stream.

To see a command-line generator that expands a curated dataset for a real feature, see [`Book Tracker: Using Evaluations to evaluate an intelligent feature`](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md).

#### Create Your Initial Dataset

Start by creating your initial dataset of samples. For guidance on dataset design principles, including golden sets, user profiles, and challenge cases, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md). Include an optional *expected* value as a benchmark if your evaluation compares model output against a known answer. For evaluations that score output without a reference answer, such as model-judge assessments of tone or fluency, omit the expected value and generate prompt-only samples.

This example builds an initial dataset for an intelligence-powered feature that converts natural-language requests into structured task items, extracting a title, due date, category, and urgency level from each free text input:

```swift
// The categories the model can assign to extracted tasks.
// The @Generable macro lets the model produce instances of this type.
@Generable
enum TaskCategory: String, Codable, Sendable {
    case work
    case personal
    case health
    case errands
    case home
}

// The structured output the model produces for each input.
@Generable
struct TaskItem: Codable, Sendable {
    var title: String
    var dueOn: String?
    var category: TaskCategory
    var isUrgent: Bool
}

let dataset: [ModelSample<TaskItem>] = [
    // Here's a health task that is non-urgent and has a due date.
    ModelSample(
        prompt: "Schedule dentist appointment for next Tuesday",
        expected: TaskItem(title: "Schedule dentist appointment",
                           dueOn: "04/07/2026", category: .health, isUrgent: false)
    ),
    // This is an errands task that is urgent and due today.
    ModelSample(
        prompt: "Buy groceries for dinner party tonight",
        expected: TaskItem(title: "Buy groceries for dinner party",
                           dueOn: "03/30/2026", category: .errands, isUrgent: true)
    ),
    // Here's a work task that's urgent and has a due date.
    ModelSample(
        prompt: "Finish quarterly report by end of week",
        expected: TaskItem(title: "Finish quarterly report",
                           dueOn: "04/03/2026", category: .work, isUrgent: true)
    ),
    // This is a home task that's non-urgent and has a due date.
    ModelSample(
        prompt: "Fix the leaky kitchen faucet this weekend",
        expected: TaskItem(title: "Fix leaky kitchen faucet",
                           dueOn: "04/05/2026", category: .home, isUrgent: false)
    ),
    // Here's a personal task that's non-urgent with no due date.
    ModelSample(
        prompt: "Learn to cook Thai food",
        expected: TaskItem(title: "Learn to cook Thai food",
                           dueOn: nil, category: .personal, isUrgent: false)
    ),
]
```

This initial dataset covers all five `TaskCategory` cases, includes both urgent and non-urgent tasks, and mixes items with and without due dates.

#### Generate Synthetic Samples

Create additional samples by calling `makeSamples(_:targetCount:sessionProvider:validator:)` with a prompt that describes the data you want to generate. For example:

```swift
let syntheticGenerationPrompt = Prompt("""
    Generate realistic to-do list items that a busy professional might have. \
    Each input is a natural-language request, and the expected output is the structured \
    task extracted from it. Cover a mix of work tasks (meetings, deadlines, \
    reviews), personal errands (shopping, appointments), health activities \
    (exercise, checkups), and home maintenance. Vary urgency and whether a \
    due date is specified.
    """)
```

The method returns an [`AsyncThrowingStream`](https://developer.apple.com/documentation/swift/asyncthrowingstream) that yields each new sample as the model generates it:

```swift
var expanded: [ModelSample<TaskItem>] = []

for try await sample in dataset.makeSamples(
    syntheticGenerationPrompt,
    targetCount: 20
) {
    expanded.append(sample)
}
```

The `targetCount` parameter sets the total size of the resulting dataset, including your initial samples. So with five initial samples and a target count of twenty, the generator produces up to fifteen new samples.

> ❗ **Important**: If you generate samples from a non-test target, such as a command-line tool that writes the dataset to disk, set “Enable Testing Search Paths” (`ENABLE_TESTING_SEARCH_PATHS`) to `YES` and add `$(DEVELOPER_DIR)/..` to “Runpath Search Paths” (`LD_RUNPATH_SEARCH_PATHS`).

#### Validate the Synthetic Samples

Use a combination of programmatic validation and manual review to catch errors, duplicates, or distribution mismatches in synthetic data before relying on it for evaluation.

Pass a `validator` closure to programmatically reject samples during generation; the closure runs once for each generated sample and returns `true` to accept it or `false` to reject it. The following example rejects any generated sample that is missing an expected value or has an empty title:

```swift
var expanded: [ModelSample<TaskItem>] = []

for try await sample in dataset.makeSamples(
    Prompt("Generate realistic to-do list items for a busy professional."),
    targetCount: 20,
    validator: { sample in
        // Reject samples that are missing an expected value or have an empty title.
        guard let task = sample.expected else { return false }
        return !task.title.isEmpty
    }
) {
    expanded.append(sample)
}
```

Review the accepted samples manually, even with a validator in place, before relying on them for evaluation:

```swift
// Print each sample's prompt alongside its extracted task for review.
for sample in expanded {
    if let task = sample.expected {
        let due = task.dueOn ?? "no date"
        let urgent = task.isUrgent ? " [URGENT]" : ""
        // Use promptDescription for printable text.
        print("\"\(sample.promptDescription)\"")
        print("  → \(task.title) (\(task.category.rawValue), \(due))\(urgent)")
    }
}
```

When you manually review the output, look for:

- **Misclassified outputs**: Check that each structured output accurately reflects its prompt. For example, confirm that a task marked `.health` actually describes a health activity, not a work meeting.
- **Category imbalance**: Watch for the model representing one category more than the others.
- **Semantic duplicates**: The generator removes identical prompts automatically, but keeps semantically similar prompts with different wording for example, “Schedule a dentist visit” and “Book a dental appointment”. Decide whether these near-duplicates help or hurt your evaluation: varied phrasings test robustness, but they can also skew your distribution if many cluster under the same category.

#### Customize the Generation Process

The `makeSamples(_:targetCount:sessionProvider:validator:)` method handles prompt construction, deduplication, and batch grouping for you. Pass a `sessionProvider` closure to control which model and instructions the generator uses:

```swift
var expanded: [ModelSample<TaskItem>] = []

for try await sample in dataset.makeSamples(
    syntheticGenerationPrompt,
    targetCount: 20,
    sessionProvider: {
        LanguageModelSession(
            // Use the Private Compute Cloud model to generate samples.
            model: PrivateCloudComputeLanguageModel(),
            instructions: """
                You create new structured task data. Generate realistic \
                to-do list items based on the examples provided. Each item \
                needs a natural prompt, an appropriate title, correct \
                category classification, and an honest urgency rating.
                """
        )
    }
) {
    expanded.append(sample)
}
```

The generator produces samples in batches of up to ten per model call. Before each batch, the generator selects a subset of your existing samples as examples in the prompt. The *sampling strategy* controls which examples appear in each model call.

The `makeSamples(_:targetCount:sessionProvider:validator:)` method always uses the default [`SampleGenerator.SamplingStrategy.random(retries:)`](samplegenerator/samplingstrategy-swift.enum/random(retries:).md) strategy, which shuffles and selects a random subset of existing samples as examples for each batch. Change the sampling strategy by creating a [`SampleGenerator`](samplegenerator.md) and set the strategy to [`SampleGenerator.SamplingStrategy.slidingWindow`](samplegenerator/samplingstrategy-swift.enum/slidingwindow.md), which steps through your samples in order so every sample gets a turn as an example. Try both and compare the output to see which works better for your data.

When you pass a validator to `makeSamples(_:targetCount:sessionProvider:validator:)`, the method silently discards any samples your validator closure rejects. Create a [`SampleGenerator`](samplegenerator.md) directly to access [`invalidSamples`](samplegenerator/invalidsamples.md) after generation completes:

```swift
let generator = SampleGenerator(
    Prompt("Generate realistic to-do list items for a busy professional."),
    samples: dataset,
    targetCount: 20,
    // Use sliding window sampling.
    samplingStrategy: .slidingWindow,
    // Reject any samples that don't have an expected value or have an empty title.
    validator: { sample in
        guard let task = sample.expected else { return false }
        return !task.title.isEmpty
    }
)

// Create the expanded dataset with the generated samples.
var expanded: [ModelSample<TaskItem>] = []
for try await sample in generator.run() {
    expanded.append(sample)
}

// Inspect the rejected samples to troubleshoot issues.
let rejected = await generator.invalidSamples
```

#### Improve Your Synthetic Generation Results

The quality of your generated samples depends on the seeds you start with, the prompts you use to expand them, and how you validate the output. For deeper guidance on each of these factors, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md).

## See Also

- [Designing datasets to test your feature](designing-evaluation-datasets.md)
  Build categorized test datasets that reflect the full range of real-world use of your feature.
- [struct ModelSample](modelsample.md)
  A general-purpose language model evaluation sample.
- [protocol Loader](loader.md)
  A protocol for types that supply a dataset for evaluation.
- [actor SampleGenerator](samplegenerator.md)
  An actor that generates evaluation samples using a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/generating-synthetic-evaluation-datasets)*