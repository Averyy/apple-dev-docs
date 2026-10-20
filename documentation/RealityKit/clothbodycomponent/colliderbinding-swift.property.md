# colliderBinding

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Configuration for binding the body to a mesh collider specified by [`sourceCollider`](./colliderbinding-swift.struct/sourcecollider.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var colliderBinding: ClothBodyComponent.ColliderBinding
```

## See Also

### Managing collisions
- [ClothBodyComponent.ColliderBinding](./colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](./collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](./enablecollisions%28towards%29.md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](./disablecollisions%28towards%29.md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.property)*