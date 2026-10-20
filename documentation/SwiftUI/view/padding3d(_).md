# padding3D(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Pads this view using the edge insets you specify.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func padding3D(_ insets: EdgeInsets3D) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func padding3D(_ length: CGFloat) -> some View
```

#### Return Value

A view that pads this view using edge the insets you specify.

## Parameters

- `insets`: The edges to inset.

## See Also

### Adding padding around a view
- [func padding(_:)](./padding%28_%29.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](./padding%28_,_%29.md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](./padding3d%28_,_%29.md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](./scenepadding%28_%29.md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](./scenepadding%28_,edges%29.md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](../scenepadding.md)
  The padding used to space a view from its containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/padding3d(_:))*