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

## Declaration

```swift
init(sampling: GenerationOptions.SamplingMode? = nil, temperature: Double? = nil, maximumResponseTokens: Int? = nil)
```

## Parameters

- `sampling`: A strategy to use for sampling from a distribution.
- `temperature`: Increasing temperature makes it possible for the model to produce less likely   responses. Must be between   and  , inclusive.
- `maximumResponseTokens`: The maximum number of tokens the model is allowed   to produce before being artificially halted. Must be positive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/init(sampling:temperature:maximumresponsetokens:))*