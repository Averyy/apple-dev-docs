# SampleGenerator

**Framework**: Evaluations  
**Kind**: class

An actor that generates evaluation samples using a language model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
actor SampleGenerator<SampleType> where SampleType : ModelSampleProtocol
```

## Mentions

- [Designing datasets to test your feature](designing-evaluation-datasets.md)
- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)
- [Designing effective evaluations](designing-effective-evaluations.md)

#### Overview

Create a generator, configure its properties, then call [`run()`](samplegenerator/run().md) to produce new samples as an async stream. After iteration completes, access [`samples`](samplegenerator/samples.md) for all generated samples, or [`invalidSamples`](samplegenerator/invalidsamples.md) for any the validator rejected.

## Topics

### Creating a generator
- [init(Prompt, samples: [SampleType], targetCount: Int, sessionProvider: (() -> LanguageModelSession)?, samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?, validator: ((SampleType) async throws -> Bool)?)](samplegenerator/init(_:samples:targetcount:sessionprovider:samplingstrategy:validator:)-2804x.md)
  Creates a generator for custom, generable evaluation samples.
- [init<T>(Prompt, samples: [SampleType], targetCount: Int, sessionProvider: (() -> LanguageModelSession)?, samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?, validator: ((SampleType) async throws -> Bool)?)](samplegenerator/init(_:samples:targetcount:sessionprovider:samplingstrategy:validator:)-8t01x.md)
  Creates a generator for sample values with a generable-expected value type.
### Configuring generation
- [var samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?](samplegenerator/samplingstrategy-swift.property.md)
  The strategy for selecting existing samples as examples in the prompt.
- [var validator: ((SampleType) async throws -> Bool)?](samplegenerator/validator.md)
  An optional closure that decides whether a generated sample is valid.
- [SampleGenerator.SamplingStrategy](samplegenerator/samplingstrategy-swift.enum.md)
  The values that define how the generator selects existing samples as examples in the generation prompt.
### Running generation
- [func run() -> some AsyncSequence<SampleType, any Error>
](samplegenerator/run.md)
  Runs the generator and returns a stream of newly synthesized samples.
### Accessing results
- [var samples: [SampleType]](samplegenerator/samples.md)
  All samples — initial and generated — from the most recent run.
- [var invalidSamples: [SampleType]](samplegenerator/invalidsamples.md)
  Samples that the validator rejected during the most recent run.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)
  Expand a small set of manually written evaluation samples into a larger dataset.
- [Designing datasets to test your feature](designing-evaluation-datasets.md)
  Build categorized test datasets that reflect the full range of real-world use of your feature.
- [struct ModelSample](modelsample.md)
  A general-purpose language model evaluation sample.
- [protocol Loader](loader.md)
  A protocol for types that supply a dataset for evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator)*