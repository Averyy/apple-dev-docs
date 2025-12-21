# teleportCharacter(to:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Moves the character instantly to a new position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func teleportCharacter(to position: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

#### Discussion

This method moves the character to a location specified relative to another entity. Pass `nil` in `relativeTo` to specify a position in world coordinates. A teleport move happens instantly. RealityKit does no collision checking when it moves the entity.

## Parameters

- `position`: The position to move the character to, relative to  .
- `referenceEntity`: The entity that defines a frame of reference.   Set this to   to indicate world space.

## See Also

- [var characterController: CharacterControllerComponent?](entity/charactercontroller.md)
  The character controller component for the entity.
- [var characterControllerState: CharacterControllerStateComponent?](entity/charactercontrollerstate.md)
  The character controller state for  the entity.
- [func moveCharacter(by: SIMD3<Float>, deltaTime: Float, relativeTo: Entity?, collisionHandler: ((CharacterControllerComponent.Collision) -> Void)?) -> CharacterControllerComponent.CollisionFlags](entity/movecharacter(by:deltatime:relativeto:collisionhandler:).md)
  Moves the character along a specified vector over a period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/teleportcharacter(to:relativeto:))*