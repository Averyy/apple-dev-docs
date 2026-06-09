# availableLanguages

**Framework**: Background Assets  
**Kind**: property

The languages for which asset packs in this manifest are localized.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var availableLanguages: [Locale.Language] { get }
```

## See Also

- [var primaryLanguage: Locale.Language?](assetpackmanifest/primarylanguage.md)
  The app’s primary language as configured in App Store Connect.
- [var resolvedLanguage: Locale.Language?](assetpackmanifest/resolvedlanguage.md)
  The language that best matches current preferences and for which a localized asset pack is available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/availablelanguages)*