# supportsLocale(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean indicating whether the given locale is supported by the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func supportsLocale(_ locale: Locale = Locale.current) -> Bool
```

## Mentions

- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Discussion

Use this method over `supportedLanguages` to check whether the given locale qualifies a user for using this model, as this method will take into consideration language fallbacks.

## See Also

- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)
  Generate content in the language people prefer when they interact with your app.
- [case unsupportedLanguageOrLocale(LanguageModelSession.GenerationError.Context)](languagemodelsession/generationerror/unsupportedlanguageorlocale(_:).md)
  An error that indicates an error that occurs if the model is prompted to respond in a language that it does not support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/supportslocale(_:))*