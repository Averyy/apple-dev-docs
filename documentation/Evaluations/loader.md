# Loader

**Framework**: Evaluations  
**Kind**: protocol

A protocol for types that supply a dataset for evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Loader<Sample> : Sendable
```

#### Overview

Use one of the built-in concrete types — [`ArrayLoader`](arrayloader.md), [`JSONLoader`](jsonloader.md), or [`StreamLoader`](streamloader.md) — or implement this protocol directly for custom data sources.

```swift
var dataset: any Loader<ModelSample<String>> {
    ArrayLoader(samples: [
        ModelSample(prompt: "One plus one is...", expected: "Two."),
        ModelSample(prompt: "Swift is...", expected: "A powerful language."),
    ])
}
```

```swift
var dataset: any Loader<ModelSample<String>> {
    JSONLoader(url: Bundle.main.url(forResource: "prompts", withExtension: "jsonl")!)
}
```

```swift
var dataset: any Loader<ModelSample<String>> {
    StreamLoader(stream: AsyncThrowingStream<ModelSample<String>, Error> { continuation in
        Task {
            let prompts = ["One plus one is...", "Swift is..."]
            for prompt in prompts {
                continuation.yield(ModelSample(prompt: prompt, expected: ""))
            }
            continuation.finish()
        }
    })
}
```

## Topics

### Loaders
- [struct ArrayLoader](arrayloader.md)
  A loader backed by an in-memory array.
- [struct JSONLoader](jsonloader.md)
  A loader backed by a JSON or JSONL file.
- [struct StreamLoader](streamloader.md)
  A loader backed by a custom async sequence.
### Associated Types
- [associatedtype Sample : SampleProtocol](loader/sample.md)
### Instance Properties
- [var stream: any AsyncSequence<Self.Sample, any Error>](loader/stream.md)
  The async sequence for iteration during an evaluation run.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [ArrayLoader](arrayloader.md)
- [JSONLoader](jsonloader.md)
- [StreamLoader](streamloader.md)

## See Also

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)
  Expand a small set of manually written evaluation samples into a larger dataset.
- [Designing datasets to test your feature](designing-evaluation-datasets.md)
  Build categorized test datasets that reflect the full range of real-world use of your feature.
- [struct ModelSample](modelsample.md)
  A general-purpose language model evaluation sample.
- [actor SampleGenerator](samplegenerator.md)
  An actor that generates evaluation samples using a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/loader)*