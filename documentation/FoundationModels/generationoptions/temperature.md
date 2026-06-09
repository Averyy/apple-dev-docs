# temperature

**Framework**: Foundation Models  
**Kind**: property

Temperature influences the confidence of the models response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
var temperature: Double?
```

#### Discussion

The value of this property must be a number between `0` and `1` inclusive.

Temperature is an adjustment applied to the probability distribution prior to sampling. A value of `1` results in no adjustment. Values less than `1` will make the probability distribution sharper, with already likely tokens becoming even more likely.

The net effect is that low temperatures manifest as more stable and predictable responses, while high temperatures give the model more creative license.

> **Note**: Leaving `temperature` nil lets the system choose a reasonable default on your behalf.

## See Also

- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](generationoptions/samplingmode-swift.property.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/temperature)*