# characterControllerState

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The character controller state for  the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var characterControllerState: CharacterControllerStateComponent? { get set }
```

## See Also

### Animating and controlling characters
- [var characterController: CharacterControllerComponent?](./charactercontroller.md)
  The character controller component for the entity.
- [func moveCharacter(by: SIMD3<Float>, deltaTime: Float, relativeTo: Entity?, collisionHandler: ((CharacterControllerComponent.Collision) -> Void)?) -> CharacterControllerComponent.CollisionFlags](./movecharacter%28by,deltatime,relativeto,collisionhandler%29.md)
  Moves the character along a specified vector over a period of time.
- [func teleportCharacter(to: SIMD3<Float>, relativeTo: Entity?)](./teleportcharacter%28to,relativeto%29.md)
  Moves the character instantly to a new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/charactercontrollerstate)*