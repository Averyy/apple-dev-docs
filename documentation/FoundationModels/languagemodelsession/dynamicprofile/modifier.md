# modifier(_:)

**Framework**: Foundation Models  
**Kind**: method

Applies a modifier to the dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func modifier<Modifier>(_ modifier: Modifier) -> some LanguageModelSession.DynamicProfile where Modifier : LanguageModelSession.DynamicProfileModifier
```

## See Also

- [func model(_:)](languagemodelsession/dynamicprofile/model(_:).md)
  Sets the model.
- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/temperature(_:).md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/samplingmode(_:).md)
  Sets the samping mode.
- [func reasoningLevel(ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/reasoninglevel(_:).md)
  Sets the reasoning level.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/maximumresponsetokens(_:).md)
  Sets the maximum response tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/modifier(_:))*