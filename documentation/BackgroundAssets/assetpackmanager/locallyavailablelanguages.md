# locallyAvailableLanguages

**Framework**: Background Assets  
**Kind**: property

The languages used by asset packs that are localized and are available locally.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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