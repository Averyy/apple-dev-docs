# GenerationOptions.SamplingMode.Kind

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

A representation of the different strategies for choosing the next token.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Kind
```

## Topics

### Sampling cases
- [GenerationOptions.SamplingMode.Kind.greedy](./kind-swift.enum/greedy.md)
  A strategy that always chooses the most likely token.
- [GenerationOptions.SamplingMode.Kind.randomProbabilityThreshold(_:seed:)](./kind-swift.enum/randomprobabilitythreshold%28_,seed%29.md)
  A strategy that samples from the highest-probability tokens whose cumulative probability reaches a threshold.
- [GenerationOptions.SamplingMode.Kind.randomTopK(_:seed:)](./kind-swift.enum/randomtopk%28_,seed%29.md)
  A strategy that samples from a fixed number of the highest-probability tokens.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the kind of sampling
- [let kind: GenerationOptions.SamplingMode.Kind](./kind-swift.property.md)
  The strategy this sampling mode uses to choose the next token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.struct/kind-swift.enum)*