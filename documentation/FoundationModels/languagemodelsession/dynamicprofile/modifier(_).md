# modifier(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

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

### Configuring the model
- [func model(_:)](./model%28_%29.md)
  Sets the model.
- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](./temperature%28_%29.md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](./samplingmode%28_%29.md)
  Sets the samping mode.
- [func reasoningLevel(ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile](./reasoninglevel%28_%29.md)
  Sets the reasoning level.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](./maximumresponsetokens%28_%29.md)
  Sets the maximum response tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/modifier(_:))*