# ScenePadding

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

Add scene padding to a view using the [`scenePadding(_:edges:)`](./view/scenepadding%28_,edges%29.md) modifier.

## Topics

### Getting padding values
- [static let minimum: ScenePadding](./scenepadding/minimum.md)
  The minimum scene padding value.
- [static let navigationBar: ScenePadding](./scenepadding/navigationbar.md)
  The navigation bar content scene padding.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding padding around a view
- [func padding(_:)](./view/padding%28_%29.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](./view/padding%28_,_%29.md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](./view/padding3d%28_%29.md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](./view/padding3d%28_,_%29.md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](./view/scenepadding%28_%29.md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](./view/scenepadding%28_,edges%29.md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenepadding)*