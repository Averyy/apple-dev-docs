# locallyAvailableLanguages

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

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

### Inspecting language support
- [var resolvedLanguage: Locale.Language?](./resolvedlanguage.md)
  The language that best matches current preferences and for which the system automatically makes localized asset packs available locally.
- [func reconcilePreferredLanguages() async throws](./reconcilepreferredlanguages%28%29.md)
  Reconciles the set of locally available asset packs with the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/locallyavailablelanguages)*