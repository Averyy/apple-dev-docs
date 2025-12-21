# CharacterControllerStateComponent

**Framework**: RealityKit  
**Kind**: struct

A component that represents the state of a character controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct CharacterControllerStateComponent
```

#### Overview

RealityKit adds this component to an entity when you add a [`CharacterControllerComponent`](charactercontrollercomponent.md) instance to it. Manually adding this component to an entity that has a character controller component has no effect because it’s redundant.

## Topics

### Creating a state component
- [init()](charactercontrollerstatecomponent/init.md)
### Accessing character controller state
- [let isOnGround: Bool](charactercontrollerstatecomponent/isonground.md)
  A Boolean value that indicates whether the character controller is on the ground.
- [let velocity: SIMD3<Float>](charactercontrollerstatecomponent/velocity.md)
  The linear speed relative to the origin in physics space.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct CharacterControllerComponent](charactercontrollercomponent.md)
  A component that manages character movement.
- [CharacterControllerComponent.Collision](charactercontrollercomponent/collision.md)
  A container that holds collision state for the character controller.
- [CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags.md)
  An option set that specifies which parts of the character capsule have collided with other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollerstatecomponent)*