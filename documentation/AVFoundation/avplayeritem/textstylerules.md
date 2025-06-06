# textStyleRules

**Framework**: AVFoundation  
**Kind**: property

An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
var textStyleRules: [AVTextStyleRule]? { get set }
```

#### Discussion

Text style rules apply only to WebVTT subtitles. They don’t apply to other subtitle formats and legible text.

## See Also

- [class AVTextStyleRule](avtextstylerule.md)
  An object that represents the text styling rules to apply to a media item’s textual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/textstylerules)*