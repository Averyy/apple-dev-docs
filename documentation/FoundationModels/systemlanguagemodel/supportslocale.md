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

- [var contextSize: Int](systemlanguagemodel/contextsize.md)
  Returns the maximum context size (in tokens) supported by the model.
- [var supportedLanguages: Set<Locale.Language>](systemlanguagemodel/supportedlanguages.md)
  Languages that the model supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/supportslocale(_:))*