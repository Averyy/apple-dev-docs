# spatialOverlayPreferenceValue(_:alignment:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@export(implementation)
nonisolated func spatialOverlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment3D = .center, @ContentBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View
```

## See Also

### Foreground elements
- [func border<S>(S, width: CGFloat) -> some View](./border%28_,width%29.md)
  Adds a border to this view with the specified style and width.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](./spatialoverlay%28alignment,content%29.md)
  Adds secondary views within the 3D bounds of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/spatialoverlaypreferencevalue(_:alignment:_:))*