# init(samplingMode:temperature:maximumResponseTokens:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates generation options that control token sampling behavior.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, visionOS 27.0)
init(samplingMode: GenerationOptions.SamplingMode? = nil, temperature: Double? = nil, maximumResponseTokens: Int? = nil)
```

## Parameters

- `samplingMode`: A strategy to use for sampling from a distribution.
- `temperature`: A value between `0` and `1`, inclusive, that controls how sharply the model favors its most likely responses. A higher value increases variety.
- `maximumResponseTokens`: The maximum number of tokens the model produces before being halted. Must be positive.

## See Also

### Creating options
- [init(samplingMode: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?, toolCallingMode: GenerationOptions.ToolCallingMode?)](./init%28samplingmode,temperature,maximumresponsetokens,toolcallingmode%29.md)
  Creates generation options that control token sampling behavior.
- [init(sampling: GenerationOptions.SamplingMode?, temperature: Double?, maximumResponseTokens: Int?)](./init%28sampling,temperature,maximumresponsetokens%29.md)
  Creates generation options that control token sampling behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/init(samplingmode:temperature:maximumresponsetokens:))*