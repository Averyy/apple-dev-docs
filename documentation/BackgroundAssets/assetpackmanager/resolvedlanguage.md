# resolvedLanguage

**Framework**: Background Assets  
**Kind**: property

The language that best matches current preferences and for which the system automatically makes localized asset packs available locally.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
var resolvedLanguage: Locale.Language? { get set }
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

The preferred languages set in Settings or System Settings inform the choice of resolved language, respecting any language that your app sets manually by setting this property. This property may be `nil` if no localized asset packs are available. You can manually set this property to `nil` to revert to the system-wide language preference. If a person using the device recently changed their preferred language, then this property’s value might be temporarily out of sync with the set of asset packs that are available locally. Setting the language doesn’t immediately download or remove any asset packs; call [`reconcilePreferredLanguages()`](assetpackmanager/reconcilepreferredlanguages().md) to reconcile the set of downloaded asset packs with the new configuration.

## See Also

- [var locallyAvailableLanguages: [Locale.Language]](assetpackmanager/locallyavailablelanguages.md)
  The languages used by asset packs that are localized and are available locally.
- [func reconcilePreferredLanguages() async throws](assetpackmanager/reconcilepreferredlanguages.md)
  Reconciles the set of locally available asset packs with the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/resolvedlanguage)*