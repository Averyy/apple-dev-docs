# CharacterControllerComponent.CollisionFlags

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An option set that specifies which parts of the character capsule have collided with other objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct CollisionFlags
```

## Topics

### Initializers
- [init(rawValue: UInt8)](./collisionflags/init%28rawvalue%29.md)
  Initializes collisions flags from a raw value.
### Instance Properties
- [let rawValue: UInt8](./collisionflags/rawvalue.md)
  The bitmask representation of the option set.
### Type Properties
- [static let bottom: CharacterControllerComponent.CollisionFlags](./collisionflags/bottom.md)
  The bottom of capsule was hit when moving in the down direction.
- [static let none: CharacterControllerComponent.CollisionFlags](./collisionflags/none.md)
  No collision.
- [static let side: CharacterControllerComponent.CollisionFlags](./collisionflags/side.md)
  The side of capsule was hit when moving in the direction tangent to the up vector.
- [static let top: CharacterControllerComponent.CollisionFlags](./collisionflags/top.md)
  The top of capsule was hit when moving in the up direction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Character control
- [struct CharacterControllerComponent](../charactercontrollercomponent.md)
  A component that manages character movement.
- [CharacterControllerComponent.Collision](./collision.md)
  A container that holds collision state for the character controller.
- [struct CharacterControllerStateComponent](../charactercontrollerstatecomponent.md)
  A component that represents the state of a character controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/collisionflags)*