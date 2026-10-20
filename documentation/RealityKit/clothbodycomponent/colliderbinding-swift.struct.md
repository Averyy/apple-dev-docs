# ClothBodyComponent.ColliderBinding

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Binds the cloth body to an entity’s mesh collider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ColliderBinding
```

#### Overview

If the binding is successful, the body particles will be constrained to stay within a configurable distance of their automatically assigned mesh collider triangles, following the collider as it deforms or moves. The per-particle [`distanceLimits`](./colliderbinding-swift.struct/distancelimits.md) controls how strictly each particle is bound.

This can be especially useful to “reset” particles back to their original positions with respect to the collider. For example, when an animated character is teleported and we want some garment the character was wearing to teleport with it in a correct manner.

The triangle on the source collider that each particle will be bound to is computed when the simulation starts, and it is chosen to be the closest triangle to the particle position at that moment.

For the best results, when using this component to attach a garment to an animated character, you should make sure that the position and shape of the collider matches the garment closely at the moment the animation starts.

## Topics

### Binding the collider
- [var sourceCollider: Entity?](./colliderbinding-swift.struct/sourcecollider.md)
  The entity containing the mesh-shaped collider that the body will bind to.
- [var isEnabled: Bool](./colliderbinding-swift.struct/isenabled.md)
  Indicates whether the cloth body should actively bind to the mesh collider.
### Tuning collision response
- [var distanceLimits: PerClothVertexData<Float>](./colliderbinding-swift.struct/distancelimits.md)
  Distance limits (in meters) for how much each particle is allowed to deviate from its perfectly-bound position.
- [var teleportThresholdSpeed: Float](./colliderbinding-swift.struct/teleportthresholdspeed.md)
  The instantaneous collider speed (in m/s) over which the source collider will be considered to have teleported.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing collisions
- [var colliderBinding: ClothBodyComponent.ColliderBinding](./colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](./colliderbinding-swift.struct/sourcecollider.md).
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](./collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](./enablecollisions%28towards%29.md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](./disablecollisions%28towards%29.md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct)*