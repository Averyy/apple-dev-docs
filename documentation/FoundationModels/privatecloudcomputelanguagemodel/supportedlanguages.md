# supportedLanguages

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

Languages that the model supports.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) final var supportedLanguages: Set<Locale.Language> { get async throws }
```

#### Discussion

To check if a given locale is considered supported by the model, use [`supportsLocale(_:)`](./supportslocale%28_%29.md), which also takes language fallbacks into consideration.

## See Also

### Handling language and locales
- [func supportsLocale(Locale) async throws -> Bool](./supportslocale%28_%29.md)
  Returns a Boolean value that indicates whether the given locale is supported by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/supportedlanguages)*