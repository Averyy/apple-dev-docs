# samplingMode

**Framework**: Foundation Models  
**Kind**: property

A sampling strategy for how the model picks tokens when generating a response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, visionOS 27.0)
var samplingMode: GenerationOptions.SamplingMode? { get set }
```

#### Discussion

When you execute a prompt on a model, the model produces a probability for every token in its vocabulary. The sampling strategy controls how the model narrows down the list of tokens to consider during that process. A strategy that picks the single most likely token yields a predictable response every time, but other strategies offer results that often sound more natural to a person.

> **Note**: Leaving the `sampling` nil lets the system choose a a reasonable default on your behalf.

## See Also

- [var temperature: Double?](generationoptions/temperature.md)
  Temperature influences the confidence of the models response.
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct.md)
  A type that defines how values are sampled from a probability distribution.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](generationoptions/toolcallingmode-swift.property.md)
  Configure the tool calling requirements.
- [GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct.md)
  A value you use to describe the model behavior when it comes to tool usage.
- [var maximumResponseTokens: Int?](generationoptions/maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/samplingmode-swift.property)*