# tipImageStyle(_:_:_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for a tip’s image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func tipImageStyle<S1, S2, S3>(_ primary: S1, _ secondary: S2, _ tertiary: S3) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
```

## See Also

- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdges: Edge.Set, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedges:action:).md)
  Presents a popover tip on the modified view.
- [func tipAnchor<AnchorID>(AnchorID) -> some View](view/tipanchor(_:).md)
  Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [func tipBackground<S>(S) -> some View](view/tipbackground(_:).md)
  Sets the tip’s view background to a style.
- [func tipBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/tipbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presented tip.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](view/tipcornerradius(_:antialiased:).md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](view/tipimagesize(_:).md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](view/tipviewstyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](view/tipimagestyle(_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](view/tipimagestyle(_:_:).md)
  Sets the style for a tip’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipimagestyle(_:_:_:))*