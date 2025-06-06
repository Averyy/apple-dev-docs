# padding3D(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Pads this view using the edge insets you specify.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func padding3D(_ edges: Edge3D.Set = .all, _ length: CGFloat? = nil) -> some View
```

#### Return Value

A view that pads this view using edge the insets you specify.

## Parameters

- `edges`: The set of edges along which to inset this view.
- `length`: The amount to inset this view on each edge. If  ,   the amount is the system default amount.

## See Also

- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](view/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](view/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](scenepadding.md)
  The padding used to space a view from its containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/padding3d(_:_:))*