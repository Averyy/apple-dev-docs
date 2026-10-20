# speedLimit

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The speed limit configuration of the simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var speedLimit: ClothSimulationComponent.SpeedLimit
```

## See Also

### Controlling simulation timing
- [var timeStep: Float](./timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [ClothSimulationComponent.SpeedLimit](./speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](./meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/speedlimit-swift.property)*