# language

**Framework**: AVKit  
**Kind**: property

The language of this media selection option.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var language: Locale.Language? { get }
```

#### Discussion

This standardized tag provides detailed language information including region, script, and variants. Returns `nil` for language-neutral content such as music-only audio tracks, sound effects, or visual-only subtitles without spoken content.

## See Also

- [var displayName: String](avinterfacemediaselectionoptionsource/displayname.md)
  Human-readable name for this media option displayed in user interfaces (e.g., “English”, “Spanish (Latin America)”, “Director’s Commentary”).
- [var identifier: String](avinterfacemediaselectionoptionsource/identifier.md)
  Unique system identifier for this media option, used for programmatic selection and persistence across sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/language)*