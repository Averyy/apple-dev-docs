# reconcilePreferredLanguages()

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Reconciles the set of locally available asset packs with the current preferred languages.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func reconcilePreferredLanguages() async throws
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

This method downloads any missing localized asset packs, waits for those downloads to finish, and removes any unneeded ones. If you’ve overridden the preferred languages by setting [`resolvedLanguage`](./resolvedlanguage.md), then this method will respect that. It won’t remove any localized asset packs that you’ve downloaded manually.

> **Throws**: When the set of locally available asset packs can’t be reconciled with the preferred languages. When the thrown error is an instance of [`AssetPackManager.LocalAvailabilityError`](./localavailabilityerror.md), it provides information about asset packs for which the system successfully ensured local availability and those for which the system couldn’t ensure local availability, with an underlying error for each failure.

## See Also

### Inspecting language support
- [var locallyAvailableLanguages: [Locale.Language]](./locallyavailablelanguages.md)
  The languages used by asset packs that are localized and are available locally.
- [var resolvedLanguage: Locale.Language?](./resolvedlanguage.md)
  The language that best matches current preferences and for which the system automatically makes localized asset packs available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/reconcilepreferredlanguages())*