# enableCollisions(towards:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Enables one-way collisions towards the selected groups for all particles in the body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func enableCollisions(towards groups: ClothCollisionGroupSet)
```

## Discussion

This adds the selected groups to the mask of all particles, causing particles in those groups to be pushed away by this body in self-collisions. Colliders are never affected by particles, so this only influences body-to-body interactions.

## Parameters

- `groups`: The collision groups to add to the mask of every particle.

## See Also

### Managing collisions
- [var colliderBinding: ClothBodyComponent.ColliderBinding](./colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](./colliderbinding-swift.struct/sourcecollider.md).
- [ClothBodyComponent.ColliderBinding](./colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](./collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func disableCollisions(towards: ClothCollisionGroupSet)](./disablecollisions%28towards%29.md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/enablecollisions(towards:))*