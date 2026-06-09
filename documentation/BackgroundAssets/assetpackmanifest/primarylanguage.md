# primaryLanguage

**Framework**: Background Assets  
**Kind**: property

The app’s primary language as configured in App Store Connect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var primaryLanguage: Locale.Language? { get }
```

#### Discussion

If no available localized asset packs match the current preferred languages, then the system falls back on the app’s primary language.

## See Also

- [var availableLanguages: [Locale.Language]](assetpackmanifest/availablelanguages.md)
  The languages for which asset packs in this manifest are localized.
- [var resolvedLanguage: Locale.Language?](assetpackmanifest/resolvedlanguage.md)
  The language that best matches current preferences and for which a localized asset pack is available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/primarylanguage)*