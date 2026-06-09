# spatialOverlayPreferenceValue(_:alignment:_:)

**Framework**: SwiftUI  
**Kind**: method

Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func spatialOverlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment3D = .center, @ContentBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View
```

## See Also

- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](view/spatialoverlay(alignment:content:).md)
  Adds secondary views within the 3D bounds of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/spatialoverlaypreferencevalue(_:alignment:_:))*