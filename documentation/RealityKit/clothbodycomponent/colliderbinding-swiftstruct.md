# ClothBodyComponent.ColliderBinding

**Framework**: RealityKit  
**Kind**: struct

Binds the cloth body to an entity’s mesh collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ColliderBinding
```

#### Overview

If the binding is successful, the body particles will be constrained to stay within a configurable distance of their automatically assigned mesh collider triangles, following the collider as it deforms or moves. The per-particle [`distanceLimits`](clothbodycomponent/colliderbinding-swift.struct/distancelimits.md) controls how strictly each particle is bound.

This can be especially useful to “reset” particles back to their original positions with respect to the collider. For example, when an animated character is teleported and we want some garment the character was wearing to teleport with it in a correct manner.

The triangle on the source collider that each particle will be bound to is computed when the simulation starts, and it is chosen to be the closest triangle to the particle position at that moment.

For the best results, when using this component to attach a garment to an animated character, you should make sure that the position and shape of the collider matches the garment closely at the moment the animation starts.

## Topics

### Binding the collider
- [var sourceCollider: Entity?](clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md)
  The entity containing the mesh-shaped collider that the body will bind to.
- [var isEnabled: Bool](clothbodycomponent/colliderbinding-swift.struct/isenabled.md)
  Indicates whether the cloth body should actively bind to the mesh collider.
### Tuning collision response
- [var distanceLimits: PerClothVertexData<Float>](clothbodycomponent/colliderbinding-swift.struct/distancelimits.md)
  Distance limits (in meters) for how much each particle is allowed to deviate from its perfectly-bound position.
- [var teleportThresholdSpeed: Float](clothbodycomponent/colliderbinding-swift.struct/teleportthresholdspeed.md)
  The instantaneous collider speed (in m/s) over which the source collider will be considered to have teleported.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var colliderBinding: ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md).
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](clothbodycomponent/collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/enablecollisions(towards:).md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/disablecollisions(towards:).md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.struct)*