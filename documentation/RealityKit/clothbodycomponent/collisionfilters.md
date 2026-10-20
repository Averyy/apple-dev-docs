# collisionFilters

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var collisionFilters: PerClothVertexData<ClothCollisionFilter> { get set }
```

#### Discussion

By default, the collision groups are set to `.defaultBodies`, and the mask is set to `.all`.

## See Also

### Managing collisions
- [var colliderBinding: ClothBodyComponent.ColliderBinding](./colliderbinding-swift.property.md)
  Configuration for binding the body to a mesh collider specified by [`sourceCollider`](./colliderbinding-swift.struct/sourcecollider.md).
- [ClothBodyComponent.ColliderBinding](./colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [func enableCollisions(towards: ClothCollisionGroupSet)](./enablecollisions%28towards%29.md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](./disablecollisions%28towards%29.md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/collisionfilters)*