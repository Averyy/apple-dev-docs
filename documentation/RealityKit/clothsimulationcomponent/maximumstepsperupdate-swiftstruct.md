# ClothSimulationComponent.MaximumStepsPerUpdate

**Framework**: RealityKit  
**Kind**: struct

The maximum number of time steps that can be processed per simulation update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MaximumStepsPerUpdate
```

## Topics

### Creating a step limit
- [static func fixed(steps: Int) -> ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct/fixed(steps:).md)
  A fixed maximum number of steps per update is manually configured.
### Describing the value
- [var debugDescription: String](clothsimulationcomponent/maximumstepsperupdate-swift.struct/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
### Type Properties
- [static var automatic: ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.struct/automatic.md)
  A dynamic maximum number of steps per update is automatically configured throughout runtime based on target platform.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var timeStep: Float](clothsimulationcomponent/timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](clothsimulationcomponent/maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](clothsimulationcomponent/speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](clothsimulationcomponent/meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/maximumstepsperupdate-swift.struct)*