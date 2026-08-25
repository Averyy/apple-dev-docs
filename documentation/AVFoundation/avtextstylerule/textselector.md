# textSelector

**Framework**: AVFoundation  
**Kind**: property

A string that identifies the text the style attributes apply to.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var textSelector: String? { get }
```

#### Discussion

The format of the legible media determines the syntax of this string. For WebVTT, it’s a CSS selector that matches the markup inside a cue. A class selector needs a leading period, and a voice selector wraps the speaker’s name in a `voice` attribute.

- **`.music`**: The text of any tag carrying the `music` class, as in `<c.music>`
- **`v[voice="Ana"]`**: The text of a voice tag that names Ana, as in `<v Ana>`
- **`::cue`**: The text of every cue

The following example applies one rule for each of those selectors:

```swift
import CoreMedia

playerItem.textStyleRules = [
    AVTextStyleRule(
        textMarkupAttributes: [kCMTextMarkupAttribute_ItalicStyle as String: true],
        textSelector: ".music"
    ),
    AVTextStyleRule(
        textMarkupAttributes: [kCMTextMarkupAttribute_ForegroundColorARGB as String: [1.0, 0.4, 0.8, 1.0]],
        textSelector: "v[voice=\"Ana\"]"
    ),
    AVTextStyleRule(
        textMarkupAttributes: [kCMTextMarkupAttribute_RelativeFontSize as String: 120],
        textSelector: "::cue"
    ),
].compactMap { $0 }
```

When this property is `nil`, the attributes act as defaults for all of the item’s text. Rules apply only where the media resource doesn’t supply equivalent styling of its own; see [`textStyleRules`](avplayeritem/textstylerules.md).

## See Also

- [var textMarkupAttributes: [String : Any]](avtextstylerule/textmarkupattributes.md)
  A dictionary of text style attributes to apply to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/textselector)*