# characterControllerState

**Framework**: RealityKit  
**Kind**: property

The character controller state for  the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var characterControllerState: CharacterControllerStateComponent? { get set }
```

## See Also

- [var characterController: CharacterControllerComponent?](entity/charactercontroller.md)
  The character controller component for the entity.
- [func moveCharacter(by: SIMD3<Float>, deltaTime: Float, relativeTo: Entity?, collisionHandler: ((CharacterControllerComponent.Collision) -> Void)?) -> CharacterControllerComponent.CollisionFlags](entity/movecharacter(by:deltatime:relativeto:collisionhandler:).md)
  Moves the character along a specified vector over a period of time.
- [func teleportCharacter(to: SIMD3<Float>, relativeTo: Entity?)](entity/teleportcharacter(to:relativeto:).md)
  Moves the character instantly to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/charactercontrollerstate)*