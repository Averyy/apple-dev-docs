# ClippingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that clips entities and their children to a customizable bounding box volume with feathered edges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClippingComponent
```

#### Overview

The `ClippingComponent` provides a powerful and performant way to clip content in RealityKit. It’s particularly useful for:

- Creating soft-edge effects with feathered boundaries instead of hard cuts
- Creating polished spatial experiences with hierarchical clipping control

Add a `ClippingComponent` to an entity by passing it to an entity’s `Entity/ComponentSet/set()` method.

```swift
let windowEntity = Entity()

let bounds = BoundingBox(min: SIMD3<Float>(-10, -10, -10), max: SIMD3<Float>(10, 10, 10))
var clipping = ClippingComponent(bounds: bounds)
clipping.featheredEdge.falloff = .linear
clipping.featheredEdge.positiveEdgeInset = [2, 2, 0.0]  // 2-unit feather zone on +X & +Y edges
clipping.featheredEdge.negativeEdgeInset = [0.0, 0.0, 0.0]  // no feathering on negative edges
clipping.shouldClipSelf = true
clipping.shouldClipChildren = true

windowEntity.components.set(clipping)
```

## Topics

### Creating a clipping component
- [init(bounds: BoundingBox)](clippingcomponent/init(bounds:).md)
### Configuring clipping behavior
- [var shouldClipChildren: Bool](clippingcomponent/shouldclipchildren.md)
  Controls whether child entities are clipped by this component’s bounds.
- [var shouldClipSelf: Bool](clippingcomponent/shouldclipself.md)
  Controls whether the entity itself is clipped by this component’s bounds.
### Feathering clipped edges
- [var featheredEdge: ClippingComponent.FeatheredEdge](clippingcomponent/featherededge-swift.property.md)
  The feathering configuration for the clipping boundaries.
- [ClippingComponent.FeatheredEdge](clippingcomponent/featherededge-swift.struct.md)
  Configuration for feathering the clipping boundaries.
### Instance Properties
- [var bounds: BoundingBox](clippingcomponent/bounds.md)
  The bounding box that defines the clipping region in the entity’s local coordinate space.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct RenderLayerComponent](renderlayercomponent.md)
  A component that defines which layers an entity participates in.
- [struct RenderLayer](renderlayer.md)
  A structured representation of render layers that provides type safety and clear semantics.
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent)*