# truncationMode

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A value that indicates how the layout truncates the last line of text to fit into the available space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var truncationMode: Text.TruncationMode { get set }
```

## Discussion

The default value is [`Text.TruncationMode.tail`](../text/truncationmode/tail.md). Some controls, however, might have a different default if appropriate.

## See Also

### Managing text layout
- [func truncationMode(Text.TruncationMode) -> some View](../view/truncationmode%28_%29.md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func allowsTightening(Bool) -> some View](../view/allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [var allowsTightening: Bool](./allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [func minimumScaleFactor(CGFloat) -> some View](../view/minimumscalefactor%28_%29.md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [func baselineOffset(CGFloat) -> some View](../view/baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func kerning(CGFloat) -> some View](../view/kerning%28_%29.md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func tracking(CGFloat) -> some View](../view/tracking%28_%29.md)
  Sets the tracking for the text in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](../view/flipsforrighttoleftlayoutdirection%28_%29.md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [enum TextAlignment](../textalignment.md)
  An alignment position for text along the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/truncationmode)*