# ClothSimulationComponent.MaximumStepsPerUpdate

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The maximum number of time steps that can be processed per simulation update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MaximumStepsPerUpdate
```

## Topics

### Creating a step limit
- [static func fixed(steps: Int) -> ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.struct/fixed%28steps%29.md)
  A fixed maximum number of steps per update is manually configured.
### Describing the value
- [var debugDescription: String](./maximumstepsperupdate-swift.struct/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
### Type Properties
- [static var automatic: ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.struct/automatic.md)
  A dynamic maximum number of steps per update is automatically configured throughout runtime based on target platform.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling simulation timing
- [var timeStep: Float](./timestep.md)
  The amount of time the simulation advances each time step, in seconds.
- [var maximumStepsPerUpdate: ClothSimulationComponent.MaximumStepsPerUpdate](./maximumstepsperupdate-swift.property.md)
  The maximum number of time steps that the simulation can advance each update.
- [var speedLimit: ClothSimulationComponent.SpeedLimit](./speedlimit-swift.property.md)
  The speed limit configuration of the simulation.
- [ClothSimulationComponent.SpeedLimit](./speedlimit-swift.struct.md)
  Whether the speed of cloth bodies should be limited to improve self-collision robustness.
- [var meshCollidersUpdateInterval: Int](./meshcollidersupdateinterval.md)
  The number of time steps between updates to the mesh colliders in the simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/maximumstepsperupdate-swift.struct)*