# inertia

**Framework**: RealityKit  
**Kind**: property

The inertia in kilograms per square meter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var inertia: SIMD3<Float>
```

#### Discussion

The vector contains the diagonal elements of the diagonalized inertia matrix.

## See Also

- [var mass: Float](physicsmassproperties/mass.md)
  The mass in kilograms.
- [var centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf)](physicsmassproperties/centerofmass.md)
  The position of the center of mass and the orientation of the principal axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties/inertia)*