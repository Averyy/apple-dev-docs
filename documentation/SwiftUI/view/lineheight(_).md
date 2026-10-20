# lineHeight(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

A modifier for the default line height in the view hierarchy.

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
func lineHeight(_ lineHeight: AttributedString.LineHeight?) -> some View
```

#### Discussion

The default value is `nil`. In that case, SwiftUI automatically chooses an appropriate line height setting for each context.

> **See Also**: [`lineHeight`](../environmentvalues/lineheight.md)

## See Also

### Text layout
- [func allowsTightening(Bool) -> some View](./allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func baselineOffset(CGFloat) -> some View](./baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](./flipsforrighttoleftlayoutdirection%28_%29.md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func kerning(CGFloat) -> some View](./kerning%28_%29.md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func minimumScaleFactor(CGFloat) -> some View](./minimumscalefactor%28_%29.md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func tracking(CGFloat) -> some View](./tracking%28_%29.md)
  Sets the tracking for the text in this view.
- [func truncationMode(Text.TruncationMode) -> some View](./truncationmode%28_%29.md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typesettingLanguage(_:isEnabled:)](./typesettinglanguage%28_,isenabled%29.md)
  Specifies the language for typesetting.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](./writingdirection%28strategy%29.md)
  A modifier for the default text writing direction strategy in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/lineheight(_:))*