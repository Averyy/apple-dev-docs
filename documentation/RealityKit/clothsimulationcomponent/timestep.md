# timeStep

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The amount of time the simulation advances each time step, in seconds.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var timeStep: Float { get set }
```

## Discussion

A smaller number means more time steps are computed each frame, leading to higher simulation accuracy but also higher computation load.

Must be positive.

## See Also

### Controlling simulation timing
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](./speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](./speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](./meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/timestep)*