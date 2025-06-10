# ScenePadding

**Framework**: SwiftUI  
**Kind**: struct

The padding used to space a view from its containing scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ScenePadding
```

#### Overview

Add scene padding to a view using the [`scenePadding(_:edges:)`](view/scenepadding(_:edges:).md) modifier.

## Topics

### Getting padding values
- [static let minimum: ScenePadding](scenepadding/minimum.md)
  The minimum scene padding value.
- [static let navigationBar: ScenePadding](scenepadding/navigationbar.md)
  The navigation bar content scene padding.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](view/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](view/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](view/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenepadding)*