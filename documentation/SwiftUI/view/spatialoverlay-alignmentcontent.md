# spatialOverlay(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method

Adds secondary views within the 3D bounds of this view.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func spatialOverlay<V>(alignment: Alignment3D = .center, @ContentBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A view that adds `content` within the view’s 3D bounds.

#### Discussion

Multiple views provided by `content` are stacked depthwise.

## Parameters

- `alignment`: The alignment with a default value of [`center`](alignment3d/center.md) that you use to position the secondary view.
- `content`: The content builder which produces views to occupy the same 3D space as this view. Multiple views provided by content are organized into a [`SpatialContainer`](spatialcontainer.md).

## See Also

- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](view/spatialoverlaypreferencevalue(_:alignment:_:).md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/spatialoverlay(alignment:content:))*