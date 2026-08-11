# maximumResponseTokens

**Framework**: Foundation Models  
**Kind**: property

The maximum number of tokens the model is allowed to produce in its response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var maximumResponseTokens: Int?
```

## Mentions

- [Managing the context window](managing-the-context-window.md)

#### Discussion

If the model produce `maximumResponseTokens` before it naturally completes its response, the framework terminates the response early, without throwing an error. Use this property to protect against unexpectedly verbose responses and runaway generations.

If no value is specified, then the model is allowed to produce the longest answer its context size supports. If the response exceeds that limit without terminating, the framework throws an error.

## See Also

- [var temperature: Double?](generationoptions/temperature.md)
  A value that influences the confidence of the model’s response.
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](generationoptions/samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct.md)
  A type that defines how values are sampled from a probability distribution.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](generationoptions/toolcallingmode-swift.property.md)
  The tool calling requirements.
- [GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct.md)
  A value you use to describe the model behavior when it comes to tool usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/maximumresponsetokens)*