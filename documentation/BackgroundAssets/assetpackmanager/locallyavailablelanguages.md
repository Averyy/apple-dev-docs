# locallyAvailableLanguages

**Framework**: Background Assets  
**Kind**: property

The languages used by asset packs that are localized and are available locally.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var locallyAvailableLanguages: [Locale.Language] { get async }
```

## See Also

- [var resolvedLanguage: Locale.Language?](assetpackmanager/resolvedlanguage.md)
  The language that best matches current preferences and for which the system automatically makes localized asset packs available locally.
- [func reconcilePreferredLanguages() async throws](assetpackmanager/reconcilepreferredlanguages.md)
  Reconciles the set of locally available asset packs with the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/locallyavailablelanguages)*