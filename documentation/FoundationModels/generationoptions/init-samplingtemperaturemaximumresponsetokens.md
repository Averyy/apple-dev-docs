# init(sampling:temperature:maximumResponseTokens:)

**Framework**: Foundation Models  
**Kind**: init

Creates generation options that control token sampling behavior.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(sampling: GenerationOptions.SamplingMode?, temperature: Double? = nil, maximumResponseTokens: Int? = nil)
```

## Parameters

- `sampling`: A strategy to use for sampling from a distribution.
- `temperature`: Increasing temperature makes it possible for the model to produce less likely responses. Must be between `0` and `1`, inclusive.
- `maximumResponseTokens`: The maximum number of tokens the model is allowed to produce before being artificially halted. Must be positive.

## See Also

- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(samplingmode:temperature:maximumresponsetokens:).md)
- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?, toolCallingMode: GenerationOptions.ToolCallingMode?)](generationoptions/init(samplingmode:temperature:maximumresponsetokens:toolcallingmode:).md)
  Creates generation options that control token sampling behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/init(sampling:temperature:maximumresponsetokens:))*