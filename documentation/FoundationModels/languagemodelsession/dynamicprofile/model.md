# model(_:)

**Framework**: Foundation Models  
**Kind**: method

Sets the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func model(_ model: any LanguageModel) -> some LanguageModelSession.DynamicProfile
```

## See Also

- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/temperature(_:).md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/samplingmode(_:).md)
  Sets the samping mode.
- [func reasoningLevel(ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/reasoninglevel(_:).md)
  Sets the reasoning level.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/maximumresponsetokens(_:).md)
  Sets the maximum response tokens.
- [func modifier<Modifier>(Modifier) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/modifier(_:).md)
  Applies a modifier to the dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/model(_:))*