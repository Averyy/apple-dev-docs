# init(shapes:mass:material:mode:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a physics body component deriving mass properties from shape and mass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency init(shapes: [ShapeResource], mass: Float, material: PhysicsMaterialResource? = nil, mode: PhysicsBodyMode = .dynamic)
```

## Parameters

- `shapes`: The shape for which to estimate the rotational inertia and center of mass.
- `mass`: The mass of the object in kilograms.
- `material`: The material properties, like friction.
- `mode`: The simulation mode that indicates how a body responds to forces.

## See Also

### Creating a physics body component
- [init()](./init%28%29.md)
  Creates a physics body component with default settings.
- [init(massProperties: PhysicsMassProperties, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](./init%28massproperties,material,mode%29.md)
  Creates a physics body component with the given mass properties, material, and mode.
- [init(shapes: [ShapeResource], density: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](./init%28shapes,density,material,mode%29.md)
  Creates a physics body component deriving mass properties from shape and density.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/init(shapes:mass:material:mode:))*