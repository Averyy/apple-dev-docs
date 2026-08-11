# supportedLanguages

**Framework**: Foundation Models  
**Kind**: property

Languages that the model supports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final var supportedLanguages: Set<Locale.Language> { get async throws }
```

#### Discussion

To check if a given locale is considered supported by the model, use [`supportsLocale(_:)`](privatecloudcomputelanguagemodel/supportslocale(_:).md), which also takes language fallbacks into consideration.

## See Also

- [func supportsLocale(Locale) async throws -> Bool](privatecloudcomputelanguagemodel/supportslocale(_:).md)
  Returns a Boolean value that indicates whether the given locale is supported by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/supportedlanguages)*