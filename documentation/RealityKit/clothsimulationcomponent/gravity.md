# gravity

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The gravitational acceleration for the bodies in the simulation, in m/s².

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var gravity: SIMD3<Float>
```

#### Discussion

Expressed in the simulation root entity’s local coordinate space.

The default value is 9.81 m/s² in the negative Y axis direction.

## See Also

### Applying forces
- [var wind: SIMD3<Float>](./wind.md)
  The wind force affecting all the cloth bodies in the simulation, in Newtons.
- [var dampingFactor: Float](./dampingfactor.md)
  The damping factor affecting all the cloth bodies in the simulation. The expected range is between 0 and 1 (included).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/gravity)*