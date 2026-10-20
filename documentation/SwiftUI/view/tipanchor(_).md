# tipAnchor(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.

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
func tipAnchor<AnchorID>(_ id: AnchorID) -> some View where AnchorID : Hashable, AnchorID : Sendable
```

#### Return Value

A new version of the view that writes to the key.

#### Discussion

Use this modifier to specify an anchor view for a `TipView`’s arrow to point towards.

```swift
struct TrailRow: View {
    let trail: Trail

    var body: some View {
        HStack {
            Text(trail.name)

            Button(action: trail.favorite) {
                Image(systemName: "star")
            }
            .tipAnchor("FavoriteTrailTipAnchor")
        }

        TipView(FavoriteTrailTip(), anchorID: "FavoriteTrailTipAnchor")
    }
}
```

## Parameters

- `id`: The anchored view’s identifier.

## See Also

- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdges: Edge.Set, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedges:action:).md)
  Presents a popover tip on the modified view.
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
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/tipimagestyle(_:_:_:).md)
  Sets the style for a tip’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipanchor(_:))*