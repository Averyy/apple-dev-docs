# CharacterControllerComponent.CollisionFlags

**Framework**: RealityKit  
**Kind**: struct

An option set that specifies which parts of the character capsule have collided with other objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct CollisionFlags
```

## Topics

### Initializers
- [init(rawValue: UInt8)](charactercontrollercomponent/collisionflags/init(rawvalue:).md)
  Initializes collisions flags from a raw value.
### Instance Properties
- [let rawValue: UInt8](charactercontrollercomponent/collisionflags/rawvalue-swift.property.md)
  The bitmask representation of the option set.
### Type Aliases
- [CharacterControllerComponent.CollisionFlags.ArrayLiteralElement](charactercontrollercomponent/collisionflags/arrayliteralelement.md)
  The type of the elements of an array literal.
- [CharacterControllerComponent.CollisionFlags.Element](charactercontrollercomponent/collisionflags/element.md)
  The element type of the option set.
- [CharacterControllerComponent.CollisionFlags.RawValue](charactercontrollercomponent/collisionflags/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let bottom: CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags/bottom.md)
  The bottom of capsule was hit when moving in the down direction.
- [static let none: CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags/none.md)
  No collision.
- [static let side: CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags/side.md)
  The side of capsule was hit when moving in the direction tangent to the up vector.
- [static let top: CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags/top.md)
  The top of capsule was hit when moving in the up direction.
### Default Implementations
- [Equatable Implementations](charactercontrollercomponent/collisionflags/equatable-implementations.md)
- [OptionSet Implementations](charactercontrollercomponent/collisionflags/optionset-implementations.md)
- [SetAlgebra Implementations](charactercontrollercomponent/collisionflags/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CharacterControllerComponent](charactercontrollercomponent.md)
  A component that manages character movement.
- [CharacterControllerComponent.Collision](charactercontrollercomponent/collision.md)
  A container that holds collision state for the character controller.
- [struct CharacterControllerStateComponent](charactercontrollerstatecomponent.md)
  A component that represents the state of a character controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/collisionflags)*