# init(shape:density:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates the mass properties for a solid shape with the specified density.

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
@preconcurrency init(shape: ShapeResource, density: Float)
```

## Parameters

- `shape`: The shape for which to calculate the mass frame.
- `density`: The density of the object in kilograms per cubic meter.

## See Also

### Creating custom mass properties
- [init()](./init%28%29.md)
  Creates a mass properties instance with default settings.
- [init(mass: Float, inertia: SIMD3<Float>, centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf))](./init%28mass,inertia,centerofmass%29.md)
  Creates a mass properties instance with the given settings.
- [init(shape: ShapeResource, mass: Float)](./init%28shape,mass%29.md)
  Creates the mass properties for a solid shape with the specified mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties/init(shape:density:))*