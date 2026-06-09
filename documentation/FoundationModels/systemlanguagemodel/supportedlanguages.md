# supportedLanguages

**Framework**: Foundation Models  
**Kind**: property

Languages that the model supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var supportedLanguages: Set<Locale.Language> { get }
```

## Mentions

- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Discussion

To check if a given locale is considered supported by the model, use `supportsLocale(_:)`, which will also take into consideration language fallbacks.

## See Also

- [var contextSize: Int](systemlanguagemodel/contextsize.md)
  Returns the maximum context size (in tokens) supported by the model.
- [func supportsLocale(Locale) -> Bool](systemlanguagemodel/supportslocale(_:).md)
  Returns a Boolean indicating whether the given locale is supported by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/supportedlanguages)*