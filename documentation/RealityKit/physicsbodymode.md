# PhysicsBodyMode

**Framework**: RealityKit  
**Kind**: enum

The ways that a physics body can move in response to physical forces.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum PhysicsBodyMode
```

## Topics

### Setting the physics body mode
- [PhysicsBodyMode.static](physicsbodymode/static.md)
  The body never moves.
- [PhysicsBodyMode.kinematic](physicsbodymode/kinematic.md)
  The user controls body movement.
- [PhysicsBodyMode.dynamic](physicsbodymode/dynamic.md)
  Forces and collisions control body movement.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct PhysicsBodyComponent](physicsbodycomponent.md)
  A component that defines an entity’s behavior in physics body simulations.
- [class PhysicsMaterialResource](physicsmaterialresource.md)
  Material properties, like friction, of a physically simulated object.
- [struct PhysicsMassProperties](physicsmassproperties.md)
  Mass properties of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodymode)*