# generateCollisionShapes(recursive:)

**Framework**: RealityKit  
**Kind**: method

Creates the shape used to detect collisions between two entities that have collision components.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func generateCollisionShapes(recursive: Bool)
```

## Mentions

- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

#### Discussion

Call this method on entities that adopt the [`HasModel`](hasmodel.md) and [`HasCollision`](hascollision.md) protocols to prepare a shape used for collision detection. The method stores the shape in the entity’s [`CollisionComponent`](collisioncomponent.md) instance.

For non-model entities, the method has no effect. Nevertheless, the method is defined for all entities so that you can call it on any entity, and have the calculation propagate recursively to all that entity’s descendants.

## Parameters

- `recursive`: A Boolean that you set to   to also generate the   collision shapes for all descendants of the entity.

## See Also

- [func generateCollisionShapes(recursive:static:)](entity/generatecollisionshapes(recursive:static:).md)
  Creates the shape used to detect collisions between two entities that have collision components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/generatecollisionshapes(recursive:))*