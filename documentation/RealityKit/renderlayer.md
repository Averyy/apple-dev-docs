# RenderLayer

**Framework**: RealityKit  
**Kind**: struct

A structured representation of render layers that provides type safety and clear semantics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderLayer
```

#### Overview

`RenderLayer` allows developers to use either named layers for custom groupings or the default layer for standard rendering behavior.

## Topics

### Accessing default layers
- [static var defaultLayer: RenderLayer](renderlayer/defaultlayer.md)
  The default layer which all meshes and lights are in unless otherwise specified
### Grouping render layers
- [RenderLayer.Set](renderlayer/set.md)
  An unordered collection of unique render layers.
### Initializers
- [init(StaticString)](renderlayer/init(_:).md)
  Creates a custom render layer with the specified compile-time constant name.
- [init?(rawValue: String)](renderlayer/init(rawvalue:).md)
  Creates a custom render layer with the specified runtime name.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct RenderLayerComponent](renderlayercomponent.md)
  A component that defines which layers an entity participates in.
- [enum PortalFactory](portalfactory.md)
  A factory for creating portal entities with simplified configuration.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct ClippingPrimitiveComponent](clippingprimitivecomponent.md)
  Use ClippingComponent instead
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer)*