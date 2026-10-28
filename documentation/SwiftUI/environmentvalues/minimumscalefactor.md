# minimumScaleFactor

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The minimum permissible proportion to shrink the font size to fit the text into the available space.

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
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

In the example below, a label with a `minimumScaleFactor` of `0.5` draws its text in a font size as small as half of the actual font if needed to fit into the space next to the text input field:

```swift
HStack {
    Text("This is a very long label:")
        .lineLimit(1)
        .minimumScaleFactor(0.5)
    TextField("My Long Text Field", text: $myTextField)
        .frame(width: 250, height: 50, alignment: .center)
}
```

![A screenshot showing the effects of setting the minimumScaleFactor on](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-minimumScaleFactor@2x.png)

You can set the minimum scale factor to any value greater than `0` and less than or equal to `1`. The default value is `1`.

SwiftUI uses this value to shrink text that doesn’t fit in a view when it’s okay to shrink the text. For example, a label with a `minimumScaleFactor` of `0.5` draws its text in a font size as small as half the actual font if needed.

## See Also

### Managing text layout
- [func truncationMode(Text.TruncationMode) -> some View](../view/truncationmode%28_%29.md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [var truncationMode: Text.TruncationMode](./truncationmode.md)
  A value that indicates how the layout truncates the last line of text to fit into the available space.
- [func allowsTightening(Bool) -> some View](../view/allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [var allowsTightening: Bool](./allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [func minimumScaleFactor(CGFloat) -> some View](../view/minimumscalefactor%28_%29.md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/minimumscalefactor)*