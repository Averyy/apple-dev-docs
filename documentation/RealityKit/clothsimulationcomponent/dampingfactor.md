# dampingFactor

**Framework**: RealityKit  
**Kind**: property

The damping factor affecting all the cloth bodies in the simulation. The expected range is between 0 and 1 (included).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var dampingFactor: Float { get set }
```

#### Discussion

Damping reduces particle velocities each time step, simulating drag from the surrounding medium. A value of 0 does not damp the body at all, so the velocities of the particles are unaltered. A value of 1 damps all movement, such that the particle velocities remain at zero.

The default value is 0

## See Also

- [var gravity: SIMD3<Float>](clothsimulationcomponent/gravity.md)
  The gravitational acceleration for the bodies in the simulation, in m/s².
- [var wind: SIMD3<Float>](clothsimulationcomponent/wind.md)
  The wind force affecting all the cloth bodies in the simulation, in Newtons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/dampingfactor)*