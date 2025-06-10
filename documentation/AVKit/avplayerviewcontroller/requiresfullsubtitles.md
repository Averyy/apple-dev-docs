# requiresFullSubtitles

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the user can disable the display of subtitles.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@MainActor
var requiresFullSubtitles: Bool { get set }
```

#### Discussion

When this property value is `true`, the subtitle menu doesn’t present the Off or Auto options, because subtitles are always displayed, if available.

The default value is `false`.

## See Also

- [var allowedSubtitleOptionLanguages: [String]?](avplayerviewcontroller/allowedsubtitleoptionlanguages.md)
  An array of language codes that restrict the set of subtitle languages available to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresfullsubtitles)*