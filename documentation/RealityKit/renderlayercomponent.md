# RenderLayerComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines which layers an entity participates in.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderLayerComponent
```

#### Overview

When attached to an entity with `ModelComponent`, it defines which layers that entity belongs to. Light components use their `layers` and shadow components use their `layers` properties to determine which entities they affect.

## Topics

### Creating a component
- [init(layer: RenderLayer)](renderlayercomponent/init(layer:).md)
  Creates a layer component with a single layer.
- [init(layers: RenderLayer.Set)](renderlayercomponent/init(layers:).md)
  Creates a layer component with the specified layers.
### Accessing render layers
- [var layers: RenderLayer.Set](renderlayercomponent/layers.md)
  The layers this entity participates in.
- [static let defaultLayer: RenderLayerComponent](renderlayercomponent/defaultlayer.md)
  The default layer used when no `RenderLayerComponent` is present.
### Initializers
- [init(RenderLayer...)](renderlayercomponent/init(_:).md)
  Creates a layer component with the specified layers.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct RenderLayer](renderlayer.md)
  A structured representation of render layers that provides type safety and clear semantics.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayercomponent)*