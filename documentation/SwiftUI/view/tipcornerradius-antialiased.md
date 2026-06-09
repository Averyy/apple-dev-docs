# tipCornerRadius(_:antialiased:)

**Framework**: SwiftUI  
**Kind**: method

Sets the corner radius for an inline tip view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func tipCornerRadius(_ cornerRadius: CGFloat, antialiased: Bool = true) -> some View
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
- [func tipImageSize(CGSize) -> some View](view/tipimagesize(_:).md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](view/tipviewstyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](view/tipimagestyle(_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](view/tipimagestyle(_:_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/tipimagestyle(_:_:_:).md)
  Sets the style for a tip’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipcornerradius(_:antialiased:))*