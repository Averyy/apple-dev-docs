# writingDirection(strategy:)

**Framework**: SwiftUI  
**Kind**: method

A modifier for the default text writing direction strategy in the view hierarchy.

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
nonisolated
func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View
```

#### Discussion

To control the writing direction explicitly, choose the [`layoutBased`](text/writingdirectionstrategy/layoutbased.md) mode and set the [`layoutDirection`](environmentvalues/layoutdirection.md) to the appropriate value.

## See Also

- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func baselineOffset(CGFloat) -> some View](view/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](view/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func kerning(CGFloat) -> some View](view/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func lineHeight(AttributedString.LineHeight?) -> some View](view/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func minimumScaleFactor(CGFloat) -> some View](view/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func tracking(CGFloat) -> some View](view/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func truncationMode(Text.TruncationMode) -> some View](view/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typesettingLanguage(_:isEnabled:)](view/typesettinglanguage(_:isenabled:).md)
  Specifies the language for typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/writingdirection(strategy:))*