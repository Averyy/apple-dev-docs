# moveCharacter(by:deltaTime:relativeTo:collisionHandler:)

**Framework**: RealityKit  
**Kind**: method

Moves the character along a specified vector over a period of time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func moveCharacter(by moveDelta: SIMD3<Float>, deltaTime: Float, relativeTo referenceEntity: Entity?, collisionHandler: ((CharacterControllerComponent.Collision) -> Void)? = nil) -> CharacterControllerComponent.CollisionFlags
```

#### Return Value

Collision flags that indicate the location of the collision.

#### Discussion

Moves the character in the collision world, with continuous collision checking and response. This will create character collision events. Entity.transform will be updated on the next engine tick. Use `CharacterControllerStateComponent` to get additional information about the state of the character after the move.

## Parameters

- `moveDelta`: Delta vector to attempt to move capsule in collision world.
- `deltaTime`: Time between last frame and current.
- `referenceEntity`: Reference entity that defines the frame of reference of the move delta.   Can be  , which is equivalent to “world space”.
- `collisionHandler`: Optional callback when an entity was hit. One call per each hit entity.

## See Also

- [func teleportCharacter(to:relativeTo:)](entity/teleportcharacter(to:relativeto:).md)
  Moves the character instantly to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/movecharacter(by:deltatime:relativeto:collisionhandler:))*