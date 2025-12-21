# DataDetector.Match.HighlightStyle

**Framework**: DataDetection  
**Kind**: enum

Values that suggest how to style a highlighted item.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum HighlightStyle
```

#### Discussion

When visually highlighting a match in some text, `HighlightStyle` suggests how to style a highlight.

- A highlight style of [`DataDetector.Match.HighlightStyle.hidden`](datadetector/match/highlightstyle/hidden.md) indicates that the match isn’t displayed. You can, however, use the match to better interpret surrounding results.
- A highlight style of [`DataDetector.Match.HighlightStyle.url`](datadetector/match/highlightstyle/url.md) indicates that the match looks like a regular web link, such as a link using the `.link` color.
- A [`DataDetector.Match.HighlightStyle.regular`](datadetector/match/highlightstyle/regular.md) highlight style indicates that the match is highlighted in a nonintrusive manner.

For instance, in iOS, the system typically displays these matches with an underline using a dimmed version of the original text color. As a suggestion for the dimmed color, when the original color is white (saturation is less than `0.02` and brightness is above `0.98`), apply an alpha value of  `0.46` to the original color. Otherwise, use a `0.26` alpha value.

Treat [`DataDetector.Match.HighlightStyle.regular`](datadetector/match/highlightstyle/regular.md)  as the default.

## Topics

### Enumeration Cases
- [DataDetector.Match.HighlightStyle.hidden](datadetector/match/highlightstyle/hidden.md)
  A highlight style that indicates the match is visually hidden from the display.
- [DataDetector.Match.HighlightStyle.regular](datadetector/match/highlightstyle/regular.md)
  A highlight style that indicates the match is accentuated in a nonintrusive manner.
- [DataDetector.Match.HighlightStyle.url](datadetector/match/highlightstyle/url.md)
  A highlight style that indicates the match displays like a regular web link.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DataDetector.Match.SemanticDetails](datadetector/match/semanticdetails.md)
  An enumeration of types of matches returned by the scanner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/highlightstyle)*