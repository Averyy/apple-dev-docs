# ClothSimulationComponent.SpeedLimit

**Framework**: RealityKit  
**Kind**: struct

Whether the speed of cloth bodies should be limited to improve self-collision robustness.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SpeedLimit
```

#### Overview

When enabled, the simulation limits particle displacement per time step to reduce the likelihood of particles tunneling through each other during self-collisions.

## Topics

### Accessing speed limits
- [static var unlimited: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct/unlimited.md)
  No speed limit, cloth bodies can move at arbitrarily fast speeds.
### Type Properties
- [static var automatic: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct/automatic.md)
  Automatically configured speed limit, which limits particle displacement per time step to reduce self-collision tunneling. The limit is proportionate to the particle density of the simulation; a higher density produces a more aggressive speed cap.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var timeStep: Float](clothsimulationcomponent/timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct.md)
  The maximum number of time steps that can be processed per simulation update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [var meshCollidersUpdateInterval: Int](clothsimulationcomponent/meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/speedlimit-swift.struct)*