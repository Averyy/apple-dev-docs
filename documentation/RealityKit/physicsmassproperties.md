# PhysicsMassProperties

**Framework**: RealityKit  
**Kind**: struct

Mass properties of a physics body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct PhysicsMassProperties
```

## Topics

### Using default mass properties
- [static let `default`: PhysicsMassProperties](physicsmassproperties/default.md)
  The default mass properties, equivalent to a unit sphere with a mass of 1 kilogram.
### Creating custom mass properties
- [init()](physicsmassproperties/init.md)
  Creates a mass properties instance with default settings.
- [init(mass: Float, inertia: SIMD3<Float>, centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf))](physicsmassproperties/init(mass:inertia:centerofmass:).md)
  Creates a mass properties instance with the given settings.
- [init(shape: ShapeResource, density: Float)](physicsmassproperties/init(shape:density:).md)
  Creates the mass properties for a solid shape with the specified density.
- [init(shape: ShapeResource, mass: Float)](physicsmassproperties/init(shape:mass:).md)
  Creates the mass properties for a solid shape with the specified mass.
### Getting mass properties
- [var mass: Float](physicsmassproperties/mass.md)
  The mass in kilograms.
- [var inertia: SIMD3<Float>](physicsmassproperties/inertia.md)
  The inertia in kilograms per square meter.
- [var centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf)](physicsmassproperties/centerofmass.md)
  The position of the center of mass and the orientation of the principal axes.
### Comparing mass properties
- [static func == (PhysicsMassProperties, PhysicsMassProperties) -> Bool](physicsmassproperties/==(_:_:).md)
  Indicates whether two physics mass properties are equal.
- [static func != (Self, Self) -> Bool](physicsmassproperties/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](physicsmassproperties/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct PhysicsBodyComponent](physicsbodycomponent.md)
  A component that defines an entity’s behavior in physics body simulations.
- [class PhysicsMaterialResource](physicsmaterialresource.md)
  Material properties, like friction, of a physically simulated object.
- [enum PhysicsBodyMode](physicsbodymode.md)
  The ways that a physics body can move in response to physical forces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties)*