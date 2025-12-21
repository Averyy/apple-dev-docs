# init(massProperties:material:mode:)

**Framework**: RealityKit  
**Kind**: init

Creates a physics body component with the given mass properties, material, and mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(massProperties: PhysicsMassProperties = .default, material: PhysicsMaterialResource? = nil, mode: PhysicsBodyMode = .dynamic)
```

## Parameters

- `massProperties`: The mass properties, like inertia.
- `material`: The material properties, like friction.
- `mode`: The simulation mode that indicates how a body responds to   forces.

## See Also

- [init()](physicsbodycomponent/init.md)
  Creates a physics body component with default settings.
- [init(shapes: [ShapeResource], density: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(shapes:density:material:mode:).md)
  Creates a physics body component deriving mass properties from shape and density.
- [init(shapes: [ShapeResource], mass: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(shapes:mass:material:mode:).md)
  Creates a physics body component deriving mass properties from shape and mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/init(massproperties:material:mode:))*