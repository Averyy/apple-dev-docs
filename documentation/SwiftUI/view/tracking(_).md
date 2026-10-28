# tracking(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the tracking for the text in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func tracking(_ tracking: CGFloat) -> some View
```

## Return Value

A view where text has the specified amount of tracking.

## Parameters

- `tracking`: The amount of additional space, in points, that the view should add to each character cluster after layout. Value of `0` sets the tracking to the system default value.

## See Also

### Managing text layout
- [func truncationMode(Text.TruncationMode) -> some View](./truncationmode%28_%29.md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [var truncationMode: Text.TruncationMode](../environmentvalues/truncationmode.md)
  A value that indicates how the layout truncates the last line of text to fit into the available space.
- [func allowsTightening(Bool) -> some View](./allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [var allowsTightening: Bool](../environmentvalues/allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [func minimumScaleFactor(CGFloat) -> some View](./minimumscalefactor%28_%29.md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [var minimumScaleFactor: CGFloat](../environmentvalues/minimumscalefactor.md)
  The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [func baselineOffset(CGFloat) -> some View](./baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func kerning(CGFloat) -> some View](./kerning%28_%29.md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](./flipsforrighttoleftlayoutdirection%28_%29.md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [enum TextAlignment](../textalignment.md)
  An alignment position for text along the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tracking(_:))*