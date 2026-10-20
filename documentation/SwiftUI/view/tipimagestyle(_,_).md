# tipImageStyle(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func tipImageStyle<S1, S2>(_ primary: S1, _ secondary: S2) -> some View where S1 : ShapeStyle, S2 : ShapeStyle
```

## See Also

### Providing tips
- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](./popovertip%28_,arrowedge,action%29.md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](./popovertip%28_,ispresented,attachmentanchor,arrowedge,action%29.md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdges: Edge.Set, action: (Tips.Action) -> Void) -> some View](./popovertip%28_,ispresented,attachmentanchor,arrowedges,action%29.md)
  Presents a popover tip on the modified view.
- [func tipAnchor<AnchorID>(AnchorID) -> some View](./tipanchor%28_%29.md)
  Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [func tipBackground<S>(S) -> some View](./tipbackground%28_%29.md)
  Sets the tip’s view background to a style.
- [func tipBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./tipbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presented tip.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](./tipcornerradius%28_,antialiased%29.md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](./tipimagesize%28_%29.md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](./tipviewstyle%28_%29.md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](./tipimagestyle%28_%29.md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](./tipimagestyle%28_,_,_%29.md)
  Sets the style for a tip’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipimagestyle(_:_:))*