# colliderBinding

**Framework**: RealityKit  
**Kind**: property

Configuration for binding the body to a mesh collider specified by [`sourceCollider`](clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var colliderBinding: ClothBodyComponent.ColliderBinding
```

## See Also

- [ClothBodyComponent.ColliderBinding](clothbodycomponent/colliderbinding-swift.struct.md)
  Binds the cloth body to an entity’s mesh collider.
- [var collisionFilters: PerClothVertexData<ClothCollisionFilter>](clothbodycomponent/collisionfilters.md)
  Defines the collision groups that each particle belongs to, and the mask used to determine which collision groups each particle is affected by.
- [func enableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/enablecollisions(towards:).md)
  Enables one-way collisions towards the selected groups for all particles in the body.
- [func disableCollisions(towards: ClothCollisionGroupSet)](clothbodycomponent/disablecollisions(towards:).md)
  Disables one-way collisions towards the selected groups for all particles in the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/colliderbinding-swift.property)*