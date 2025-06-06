# init(mass:inertia:centerOfMass:)

**Framework**: RealityKit  
**Kind**: init

Creates a mass properties instance with the given settings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
init(mass: Float, inertia: SIMD3<Float> = SIMD3<Float>(x: 0.1, y: 0.1, z: 0.1), centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf) = (SIMD3<Float>(x: 0, y: 0, z: 0), simd_quatf(ix: 0, iy: 0, iz: 0, r: 1)))
```

## Parameters

- `mass`: The mass in kilograms. If you use a mass of   or infinity, the   simulation treats the object as  . That is,   the object doesn’t respond to forces.
- `inertia`: The inertia in kilograms per square meter. The vector   contains the diagonal elements of the diagonalized inertia matrix.
- `centerOfMass`: The   defines the principal axes, such the inertia matrix is a diagonal.

## See Also

- [init()](physicsmassproperties/init.md)
  Creates a mass properties instance with default settings.
- [init(shape: ShapeResource, density: Float)](physicsmassproperties/init(shape:density:).md)
  Creates the mass properties for a solid shape with the specified density.
- [init(shape: ShapeResource, mass: Float)](physicsmassproperties/init(shape:mass:).md)
  Creates the mass properties for a solid shape with the specified mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties/init(mass:inertia:centerofmass:))*