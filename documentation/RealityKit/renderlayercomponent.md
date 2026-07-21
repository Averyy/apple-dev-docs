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

Add a [`RenderLayerComponent`](renderlayercomponent.md) to an entity to control which lights illuminate it and which lights it casts shadows from. A light affects this entity when the entity’s [`layers`](renderlayercomponent/layers.md) intersect with the light’s layers, for example [`layers`](directionallightcomponent/layers.md), [`layers`](pointlightcomponent/layers.md), or [`layers`](spotlightcomponent/layers.md).

Entities without a [`RenderLayerComponent`](renderlayercomponent.md) are treated as members of [`defaultLayer`](renderlayer/defaultlayer.md).

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
  A render layer component that contains only [`defaultLayer`](renderlayer/defaultlayer.md).
### Initializers
- [init(RenderLayer...)](renderlayercomponent/init(_:).md)
  Creates a layer component with the specified layers.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct RenderLayer](renderlayer.md)
  A named identifier for a group of meshes and lights.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayercomponent)*