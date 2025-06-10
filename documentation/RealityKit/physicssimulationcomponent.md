# PhysicsSimulationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that controls localized physics simulations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct PhysicsSimulationComponent
```

#### Overview

Simulate local physics by adding a [`PhysicsSimulationComponent`](physicssimulationcomponent.md) to an entity. The component gives your app the ability to customize the physics simulation by configuring its properties, such as [`gravity`](physicssimulationcomponent/gravity.md) and [`collisionOptions`](physicssimulationcomponent/collisionoptions-swift.property.md).

> ❗ **Important**: Each physics simulation component uses meters as its unit of distance, which can be important to other types in the physics simulation, such as [`ShapeResource`](shaperesource.md) instances.

## Topics

### Structures
- [PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.struct.md)
  The options set that defines how a physics simulation reports collisions.
- [PhysicsSimulationComponent.SolverIterations](physicssimulationcomponent/solveriterations-swift.struct.md)
  The parameters that control the accuracy of solving physics simulations.
### Initializers
- [init()](physicssimulationcomponent/init.md)
### Instance Properties
- [var clock: CMClockOrTimebase](physicssimulationcomponent/clock.md)
  A custom clock which drives the physics simulation, defaults to the engine clock.
- [var collisionOptions: PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.property.md)
  Options for kinematic collision reporting.
- [var gravity: SIMD3<Float>](physicssimulationcomponent/gravity.md)
  The gravity for the simulation relative to the simulation entity.
- [var solverIterations: PhysicsSimulationComponent.SolverIterations](physicssimulationcomponent/solveriterations-swift.property.md)
  The parameters that control the accuracy of solving physics simulations.
### Type Methods
- [static func nearestSimulationEntity(for: Entity) -> Entity?](physicssimulationcomponent/nearestsimulationentity(for:).md)
  Obtains the entity containing the physics simulation origin.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)
  Configure your RealityKit scenes to avoid performance bottlenecks.
- [Handling different-sized objects in physics simulations](handling-different-sized-objects-in-physics-simulations.md)
  Set up a scene hierarchy for accurate physics simulations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationcomponent)*