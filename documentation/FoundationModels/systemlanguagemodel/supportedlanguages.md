# supportedLanguages

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

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

- [Supporting languages and locales with Foundation Models](../supporting-languages-and-locales-with-foundation-models.md)

## Discussion

To check if a given locale is considered supported by the model, use [`supportsLocale(_:)`](./supportslocale%28_%29.md), which also takes language fallbacks into consideration.

## See Also

### Inspecting model capabilities
- [var contextSize: Int](./contextsize.md)
  The maximum context size in tokens that the model supports.
- [func supportsLocale(Locale) -> Bool](./supportslocale%28_%29.md)
  Returns a Boolean value that indicates whether the given locale is supported by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/supportedlanguages)*