# supportsLocale(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean value that indicates whether the given locale is supported by the model.

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
(nonsending) final func supportsLocale(_ locale: Locale = Locale.current) async throws -> Bool
```

#### Discussion

Use this method over [`supportedLanguages`](privatecloudcomputelanguagemodel/supportedlanguages.md) to check whether the given locale qualifies a person for using this model, as this method also takes language fallbacks into consideration.

## See Also

- [var supportedLanguages: Set<Locale.Language>](privatecloudcomputelanguagemodel/supportedlanguages.md)
  Languages that the model supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/supportslocale(_:))*