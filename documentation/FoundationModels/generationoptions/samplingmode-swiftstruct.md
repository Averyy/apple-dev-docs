# GenerationOptions.SamplingMode

**Framework**: Foundation Models  
**Kind**: struct

A type that defines how values are sampled from a probability distribution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct SamplingMode
```

#### Overview

A model builds its response to a prompt in a loop. At each iteration in the loop the model produces a probability distribution for all the tokens in its vocabulary. The sampling mode controls how a token is selected from that distribution.

## Topics

### Sampling modes
- [static var greedy: GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct/greedy.md)
  A sampling mode that always chooses the most likely token.
- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct/random(probabilitythreshold:seed:).md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct/random(top:seed:).md)
  A sampling mode that considers a fixed number of high-probability tokens.
### Getting the kind of sampling
- [let kind: GenerationOptions.SamplingMode.Kind](generationoptions/samplingmode-swift.struct/kind-swift.property.md)
- [GenerationOptions.SamplingMode.Kind](generationoptions/samplingmode-swift.struct/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var temperature: Double?](generationoptions/temperature.md)
  A value that influences the confidence of the model’s response.
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](generationoptions/samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](generationoptions/toolcallingmode-swift.property.md)
  The tool calling requirements.
- [GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct.md)
  A value you use to describe the model behavior when it comes to tool usage.
- [var maximumResponseTokens: Int?](generationoptions/maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.struct)*