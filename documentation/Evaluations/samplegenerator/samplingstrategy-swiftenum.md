# SampleGenerator.SamplingStrategy

**Framework**: Evaluations  
**Kind**: enum

The values that define how the generator selects existing samples as examples in the generation prompt.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SamplingStrategy
```

#### Overview

When a model repeats an inference, the strategy determines whether and how the generator retries with different examples.

## Topics

### Strategies
- [SampleGenerator.SamplingStrategy.random(retries:)](samplegenerator/samplingstrategy-swift.enum/random(retries:).md)
  A strategy that randomly picks a subset of samples each time a model repeats inference.
- [SampleGenerator.SamplingStrategy.slidingWindow](samplegenerator/samplingstrategy-swift.enum/slidingwindow.md)
  A strategy that slides a window through the examples, advancing it each batch.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var samplingStrategy: SampleGenerator<SampleType>.SamplingStrategy?](samplegenerator/samplingstrategy-swift.property.md)
  The strategy for selecting existing samples as examples in the prompt.
- [var validator: ((SampleType) async throws -> Bool)?](samplegenerator/validator.md)
  An optional closure that decides whether a generated sample is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samplingstrategy-swift.enum)*