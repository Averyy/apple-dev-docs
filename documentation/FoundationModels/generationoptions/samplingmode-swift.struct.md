# GenerationOptions.SamplingMode

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that defines how values are sampled from a probability distribution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct SamplingMode
```

## Overview

A model builds its response to a prompt in a loop. At each iteration in the loop the model produces a probability distribution for all the tokens in its vocabulary. The sampling mode controls how a token is selected from that distribution.

## Topics

### Sampling modes
- [static var greedy: GenerationOptions.SamplingMode](./samplingmode-swift.struct/greedy.md)
  A sampling mode that always chooses the most likely token.
- [static func random(probabilityThreshold: Double, seed: UInt64?) -> GenerationOptions.SamplingMode](./samplingmode-swift.struct/random%28probabilitythreshold,seed%29.md)
  A mode that considers a variable number of high-probability tokens based on the specified threshold.
- [static func random(top: Int, seed: UInt64?) -> GenerationOptions.SamplingMode](./samplingmode-swift.struct/random%28top,seed%29.md)
  A sampling mode that considers a fixed number of high-probability tokens.
### Getting the kind of sampling
- [let kind: GenerationOptions.SamplingMode.Kind](./samplingmode-swift.struct/kind-swift.property.md)
  The strategy this sampling mode uses to choose the next token.
- [GenerationOptions.SamplingMode.Kind](./samplingmode-swift.struct/kind-swift.enum.md)
  A representation of the different strategies for choosing the next token.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring options
- [var temperature: Double?](./temperature.md)
  A value that influences the confidence of the model’s response.
- [var sampling: GenerationOptions.SamplingMode?](./sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](./samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](./toolcallingmode-swift.property.md)
  The tool calling requirements.
- [GenerationOptions.ToolCallingMode](./toolcallingmode-swift.struct.md)
  A value that describes how the model uses tools.
- [var maximumResponseTokens: Int?](./maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.struct)*