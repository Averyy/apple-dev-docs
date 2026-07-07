# maximumStepsPerUpdate

**Framework**: RealityKit  
**Kind**: property

The maximum number of time steps that the simulation can advance each update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate
```

#### Discussion

A higher number of time steps per update is more expensive in terms of power and performance. However, a lower number restricts the simulation’s ability to keep up with the [`targetClock`](clothsimulationcomponent/targetclock.md).

As an example, if [`timeStep`](clothsimulationcomponent/timestep.md) is `1.4 ms` and [`maximumStepsPerUpdate`](clothsimulationcomponent/maximumstepsperupdate-swift.property.md) is `13`, then the simulation can perfectly follow [`targetClock`](clothsimulationcomponent/targetclock.md) up to delta times of `1.4 ms * 13 = 18.2 ms`.

The automatic value differs based on the target platform. Must be a positive number.

## See Also

- [var timeStep: Float](clothsimulationcomponent/timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](clothsimulationcomponent/meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/maximumstepsperupdate-swift.property)*