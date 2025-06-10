# init(shapes:density:material:mode:)

**Framework**: RealityKit  
**Kind**: init

Creates a physics body component deriving mass properties from shape and density.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(shapes: [ShapeResource], density: Float, material: PhysicsMaterialResource? = nil, mode: PhysicsBodyMode = .dynamic)
```

## Mentions

- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)

## Parameters

- `shapes`: The shape for which to estimate the mass, rotational inertia,   and center of mass.
- `density`: The density of the object in kilograms per cubic meter.
- `material`: The material properties, like friction.
- `mode`: The simulation mode that indicates how a body responds to   forces.

## See Also

- [init()](physicsbodycomponent/init.md)
  Creates a physics body component with default settings.
- [init(massProperties: PhysicsMassProperties, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(massproperties:material:mode:).md)
  Creates a physics body component with the given mass properties, material, and mode.
- [init(shapes: [ShapeResource], mass: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(shapes:mass:material:mode:).md)
  Creates a physics body component deriving mass properties from shape and mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/init(shapes:density:material:mode:))*