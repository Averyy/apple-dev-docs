# OcclusionCullingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OcclusionCullingComponent
```

#### Overview

Occlusion culling can improve performance by skipping rendering for entities that are fully hidden behind other geometry. Entities are opted into this system by default.

This component can be used to disable occlusion culling for an Entity hierarchy if it’s observed that culling produces incorrect visuals. Such scenarios may include:

- Content that quickly moves in and out of occluded areas.
- Content that uses a Geometry Modifier to warp vertices outside of the mesh’s reported bounds.
- A camera teleports to a new location in a single frame and starts viewing the scene from a drastically different angle or position.

The enablement setting on this component will be applied recursively to descendant Entities. A component added to a descendant Entity will override any settings inherited from its parent.

## Topics

### Creating a component
- [init(isEnabled: Bool)](occlusioncullingcomponent/init(isenabled:).md)
### Enabling occlusion culling
- [var isEnabled: Bool](occlusioncullingcomponent/isenabled.md)
  Whether occlusion culling should be performed on this Entity and its children.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct RenderLayerComponent](renderlayercomponent.md)
  A component that defines which layers an entity participates in.
- [struct RenderLayer](renderlayer.md)
  A structured representation of render layers that provides type safety and clear semantics.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/occlusioncullingcomponent)*