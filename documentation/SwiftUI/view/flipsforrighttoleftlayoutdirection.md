# flipsForRightToLeftLayoutDirection(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.

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
func flipsForRightToLeftLayoutDirection(_ enabled: Bool) -> some View
```

#### Return Value

A view that conditionally mirrors its contents horizontally when the layout direction is right-to-left.

#### Discussion

Use `flipsForRightToLeftLayoutDirection(_:)` when you need the system to horizontally mirror the contents of the view when presented in a right-to-left layout.

To override the layout direction for a specific view, use the [`environment(_:_:)`](view/environment(_:_:).md) view modifier to explicitly override the [`layoutDirection`](environmentvalues/layoutdirection.md) environment value for the view.

## Parameters

- `enabled`: A Boolean value that indicates whether this view   should have its content flipped horizontally when the layout   direction is right-to-left. By default, views will adjust their layouts   automatically in a right-to-left context and do not need to be mirrored.

## See Also

- [func truncationMode(Text.TruncationMode) -> some View](view/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
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
- [enum TextAlignment](textalignment.md)
  An alignment position for text along the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/flipsforrighttoleftlayoutdirection(_:))*