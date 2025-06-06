# mass

**Framework**: RealityKit  
**Kind**: property

The mass in kilograms.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var mass: Float
```

#### Discussion

For a mass of `0` or infinity, the simulation treats the object as [`PhysicsBodyMode.kinematic`](physicsbodymode/kinematic.md). That is, the object doesn’t respond to forces.

## See Also

- [var inertia: SIMD3<Float>](physicsmassproperties/inertia.md)
  The inertia in kilograms per square meter.
- [var centerOfMass: (position: SIMD3<Float>, orientation: simd_quatf)](physicsmassproperties/centerofmass.md)
  The position of the center of mass and the orientation of the principal axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmassproperties/mass)*