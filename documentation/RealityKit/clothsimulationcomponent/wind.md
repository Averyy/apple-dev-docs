# wind

**Framework**: RealityKit  
**Kind**: property

The wind force affecting all the cloth bodies in the simulation, in Newtons.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var wind: SIMD3<Float>
```

#### Discussion

The magnitude of the force applied to each particle depends on the angle between the wind direction and the particle’s normal. Full force is applied when the wind is aligned with the normal, and no force is applied when the wind is perpendicular to the normal.

Expressed in the simulation root entity’s local coordinate space. The default value is (0, 0, 0).

## See Also

- [var gravity: SIMD3<Float>](clothsimulationcomponent/gravity.md)
  The gravitational acceleration for the bodies in the simulation, in m/s².
- [var dampingFactor: Float](clothsimulationcomponent/dampingfactor.md)
  The damping factor affecting all the cloth bodies in the simulation. The expected range is between 0 and 1 (included).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/wind)*