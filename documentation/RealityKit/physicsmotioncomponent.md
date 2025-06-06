# PhysicsMotionComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls the motion of the body in physics simulations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct PhysicsMotionComponent
```

## Mentions

- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)

#### Overview

You specify velocities in the coordinate space of the physics simulation defined by [`nearestSimulationEntity(for:)`](physicssimulationcomponent/nearestsimulationentity(for:).md).

The behavior of an entity with a physics motion component depends on the entity’s [`mode`](physicsbodycomponent/mode.md) setting:

## Topics

### Creating the motion component
- [init()](physicsmotioncomponent/init.md)
  Creates a physics motion component at rest.
- [init(linearVelocity: SIMD3<Float>, angularVelocity: SIMD3<Float>)](physicsmotioncomponent/init(linearvelocity:angularvelocity:).md)
  Creates a physics motion component with the given velocities.
### Setting velocity
- [var angularVelocity: SIMD3<Float>](physicsmotioncomponent/angularvelocity.md)
  The angular velocity of the body around the center of mass.
- [var linearVelocity: SIMD3<Float>](physicsmotioncomponent/linearvelocity.md)
  The linear velocity of the body in the physics simulation.
### Registering a component type
- [static func registerComponent()](physicsmotioncomponent/registercomponent.md)
  Registers a new component type.
### Comparing physics motion components
- [static func == (PhysicsMotionComponent, PhysicsMotionComponent) -> Bool](physicsmotioncomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](physicsmotioncomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Component Implementations](physicsmotioncomponent/component-implementations.md)
- [Equatable Implementations](physicsmotioncomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct ImpulseAction](impulseaction.md)
  An action that applies an impulse to the physics body at its center of mass when played as an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmotioncomponent)*