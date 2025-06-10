# allowedSubtitleOptionLanguages

**Framework**: AVKit  
**Kind**: property

An array of language codes that restrict the set of subtitle languages available to the user.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@MainActor
var allowedSubtitleOptionLanguages: [String]? { get set }
```

#### Discussion

When this property value is `nil` (the default), the player view controller UI presents all available subtitle options. The Auto subtitle option is only available when this property value is `nil` and [`requiresFullSubtitles`](avplayerviewcontroller/requiresfullsubtitles.md) is `false`.

To allow only a restricted subset of subtitles, set this property value to an array of BCP 47 language codes. Restricting the set of subtitle languages makes the Auto option unavailable.

## See Also

- [var requiresFullSubtitles: Bool](avplayerviewcontroller/requiresfullsubtitles.md)
  A Boolean value that indicates whether the user can disable the display of subtitles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowedsubtitleoptionlanguages)*