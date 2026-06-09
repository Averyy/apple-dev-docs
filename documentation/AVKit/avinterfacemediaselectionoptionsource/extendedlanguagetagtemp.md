# extendedLanguageTagTemp

**Framework**: AVKit  
**Kind**: property

IETF BCP 47 language identifier represented as a `Locale.Language`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var extendedLanguageTagTemp: Locale.Language? { get }
```

#### Discussion

This standardized tag provides detailed language information including region, script, and variants. Returns `nil` for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/extendedlanguagetagtemp)*