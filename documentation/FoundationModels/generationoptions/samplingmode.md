# GenerationOptions.SamplingMode

**Framework**: Foundation Models  
**Kind**: struct

A type that defines how values are sampled from a probability distribution.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct SamplingMode
```

#### Overview

A model builds its response to a prompt in a loop. At each iteration in the loop the model produces a probability distribution for all the tokens in its vocabulary. The sampling mode controls how a token is selected from that distribution.

## Topics

### Sampling options
- [static var greedy: GenerationOptions.SamplingMode](generationoptions/samplingmode/greedy.md)
  A sampling mode that always chooses the most likely token.
- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(probabilitythreshold:seed:).md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode/random(top:seed:).md)
  A sampling mode that considers a fixed number of high-probability tokens.
### Comparing sampling modes
- [static func == (GenerationOptions.SamplingMode, GenerationOptions.SamplingMode) -> Bool](generationoptions/samplingmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](generationoptions/samplingmode/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode)*