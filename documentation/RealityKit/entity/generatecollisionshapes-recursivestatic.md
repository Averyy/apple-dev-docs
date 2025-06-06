# generateCollisionShapes(recursive:static:)

**Framework**: RealityKit  
**Kind**: method

Creates the shape used to detect collisions between two entities that have collision components.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func generateCollisionShapes(recursive: Bool, static isStatic: Bool)
```

#### Discussion

Call this method on entities that adopt the [`HasModel`](hasmodel.md) and [`HasCollision`](hascollision.md) protocols to prepare a shape used for collision detection. The method stores the shape in the entity’s [`CollisionComponent`](collisioncomponent.md) instance.

For non-model entities, the method has no effect. Nevertheless, the method is defined for all entities so that you can call it on any entity, and have the calculation propagate recursively to all that entity’s descendants.

## Parameters

- `recursive`: A Boolean that you set to   to also generate the   collision shapes for all descendants of the entity.
- `isStatic`: A Boolean value that indicates whether the colliders move. Set this to   to indicate the colliders don’t move.   Non-moving, static colliders are more efficient to use than non-static ones.

## See Also

- [func generateCollisionShapes(recursive: Bool)](entity/generatecollisionshapes(recursive:).md)
  Creates the shape used to detect collisions between two entities that have collision components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/generatecollisionshapes(recursive:static:))*