# init(samplingMode:temperature:maximumResponseTokens:toolCallingMode:)

**Framework**: Foundation Models  
**Kind**: init

Creates generation options that control token sampling behavior.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(samplingMode: GenerationOptions.SamplingMode? = nil, temperature: Double? = nil, maximumResponseTokens: Int? = nil, toolCallingMode: GenerationOptions.ToolCallingMode?)
```

## Parameters

- `samplingMode`: A strategy to use for sampling from a distribution.
- `temperature`: A value between `0` and `1`, inclusive, that controls how sharply the model favors its most likely responses. A higher value increases variety.
- `maximumResponseTokens`: The maximum number of tokens the model is allowed to produce before being artificially halted. Must be positive.

## See Also

- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(samplingmode:temperature:maximumresponsetokens:).md)
- [init(sampling: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](generationoptions/init(sampling:temperature:maximumresponsetokens:).md)
  Creates generation options that control token sampling behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/init(samplingmode:temperature:maximumresponsetokens:toolcallingmode:))*