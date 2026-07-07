# disableCollisions(towards:)

**Framework**: RealityKit  
**Kind**: method

Disables one-way collisions towards the selected groups for all particles in the body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func disableCollisions(towards groups: ClothCollisionGroupSet)
```

#### Discussion

This removes the selected groups from the mask of all particles, so that particles in those groups will no longer be pushed away by this body in self-collisions. Colliders are never affected by particles, so this only influences body-to-body interactions.

## Parameters

- `groups`: The collision groups to remove from the mask of every particle.

## See Also

- [var colliderBinding: ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md).
- [ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](clothbodycomponent/collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/enablecollisions(towards:).md)
  Enables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/disablecollisions(towards:))*