# RenderLayer

**Framework**: RealityKit  
**Kind**: struct

A named identifier for a group of meshes and lights.

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

Use a [`RenderLayer`](renderlayer.md) to associate a light with the entities it should illuminate, or to mark which entities a light affects. Every entity belongs to [`defaultLayer`](renderlayer/defaultlayer.md) unless its [`RenderLayerComponent`](renderlayercomponent.md) specifies otherwise.

Define your own layers as static constants in an extension so they’re easy to reuse:

```swift
extension RenderLayer {
    static let hero = RenderLayer("com.myapp.hero")
    static let background = RenderLayer("com.myapp.background")
}
```

## Topics

### Accessing default layers
- [static var defaultLayer: RenderLayer](renderlayer/defaultlayer.md)
  The default layer.
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
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer)*