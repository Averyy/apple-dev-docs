# tipBackgroundInteraction(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls whether people can interact with the view behind a presented tip.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func tipBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
```

##### Discussion

On many platforms, SwiftUI automatically disables the view behind a popover tip that you present, so that people can’t interact with the backing view until they dismiss the tip. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind a `popoverTip`.

```swift
struct LandmarkDetail: View {
    let landmark: Landmark

    var body: some View {
        ScrollView {
            MapView(coordinate: landmark.locationCoordinate)
                .popoverTip(CampsiteTip())
                .tipBackgroundInteraction(.enabled)

            HStack {
                Text(landmark.name)
                Text(landmark.park)
            }
        }
    }
}
```

## Parameters

- `interaction`: A specification of how people can interact with the view behind a presented tip.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tipbackgroundinteraction(_:))*