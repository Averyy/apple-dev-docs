# supportsLocale(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean indicating whether the given locale is supported by the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func supportsLocale(_ locale: Locale = Locale.current) -> Bool
```

#### Discussion

Use this method over `supportedLanguages` to check whether the given locale qualifies a user for using this model, as this method will take into consideration language fallbacks.

## See Also

- [var supportedLanguages: Set<Locale.Language>](privatecloudcomputelanguagemodel/supportedlanguages.md)
  Languages that the model supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/supportslocale(_:))*