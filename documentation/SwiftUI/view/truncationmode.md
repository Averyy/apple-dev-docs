# truncationMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the truncation mode for lines of text that are too long to fit in the available space.

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
nonisolated
func truncationMode(_ mode: Text.TruncationMode) -> some View
```

#### Return Value

A view that truncates text at different points in a line depending on the mode you select.

#### Discussion

Use the `truncationMode(_:)` modifier to determine whether text in a long line is truncated at the beginning, middle, or end. Truncation is indicated by adding an ellipsis (…) to the line when removing text to indicate to readers that text is missing.

In the example below, the bounds of text view constrains the amount of text that the view displays and the `truncationMode(_:)` specifies from which direction and where to display the truncation indicator:

```swift
Text("This is a block of text that will show up in a text element as multiple lines. The text will fill the available space, and then, eventually, be truncated.")
    .frame(width: 150, height: 150)
    .truncationMode(.tail)
```

![A screenshot showing the effect of truncation mode on text in a](https://docs-assets.developer.apple.com/published/d15db793ff442f002c0fb57cbd7f14dc/SwiftUI-view-truncationMode%402x.png)

## Parameters

- `mode`: The truncation mode that specifies where to truncate   the text within the text view, if needed. You can truncate at the   beginning, middle, or end of the text view.

## See Also

- [var truncationMode: Text.TruncationMode](environmentvalues/truncationmode.md)
  A value that indicates how the layout truncates the last line of text to fit into the available space.
- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [var allowsTightening: Bool](environmentvalues/allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [func minimumScaleFactor(CGFloat) -> some View](view/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [var minimumScaleFactor: CGFloat](environmentvalues/minimumscalefactor.md)
  The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [func baselineOffset(CGFloat) -> some View](view/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func kerning(CGFloat) -> some View](view/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func tracking(CGFloat) -> some View](view/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](view/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [enum TextAlignment](textalignment.md)
  An alignment position for text along the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/truncationmode(_:))*