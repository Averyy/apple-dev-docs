# timeStep

**Framework**: RealityKit  
**Kind**: property

The amount of time the simulation advances each time step, in seconds.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var timeStep: Float { get set }
```

#### Discussion

A smaller number means more time steps are computed each frame, leading to higher simulation accuracy but also higher computation load.

Must be positive.

## See Also

- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](clothsimulationcomponent/meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/timestep)*