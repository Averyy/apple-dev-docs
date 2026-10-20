# reasoningLevel(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Sets the reasoning level.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func reasoningLevel(_ reasoningLevel: ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile
```

## See Also

### Configuring the model
- [func model(_:)](./model%28_%29.md)
  Sets the model.
- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](./temperature%28_%29.md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](./samplingmode%28_%29.md)
  Sets the samping mode.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](./maximumresponsetokens%28_%29.md)
  Sets the maximum response tokens.
- [func modifier<Modifier>(Modifier) -> some LanguageModelSession.DynamicProfile](./modifier%28_%29.md)
  Applies a modifier to the dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/reasoninglevel(_:))*