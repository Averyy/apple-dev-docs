# centerOfMass

**Framework**: RealityKit  
**Kind**: property

The position of the center of mass and the orientation of the principal axes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf)
```

#### Discussion

The `position` defines the center of mass with a default value of `(0, 0, 0)`, which means that the local origin of the model is the center of mass.

The `orientation` defines the principal axes, such the inertia matrix is a diagonal.

## See Also

- [var mass: Float](physicsmassproperties/mass.md)
  The mass in kilograms.
- [var inertia: SIMD3<Float>](physicsmassproperties/inertia.md)
  The inertia in kilograms per square meter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties/centerofmass)*