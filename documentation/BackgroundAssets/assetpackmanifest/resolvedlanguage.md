# resolvedLanguage

**Framework**: Background Assets  
**Kind**: property

The language that best matches current preferences and for which a localized asset pack is available locally.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var resolvedLanguage: Locale.Language? { get }
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

The preferred languages set in Settings or System Settings inform the choice of resolved language, respecting any language that your app sets manually by setting [`resolvedLanguage`](assetpackmanager/resolvedlanguage.md). This property may be `nil` if no localized asset packs are available. If a person using the device recently changed their preferred language or if this manifest is outdated, then this property’s value may be out of sync with the set of asset packs that are available locally.

## See Also

- [var primaryLanguage: Locale.Language?](assetpackmanifest/primarylanguage.md)
  The app’s primary language as configured in App Store Connect.
- [var availableLanguages: [Locale.Language]](assetpackmanifest/availablelanguages.md)
  The languages for which asset packs in this manifest are localized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/resolvedlanguage)*