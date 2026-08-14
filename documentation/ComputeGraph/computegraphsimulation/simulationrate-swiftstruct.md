# ComputeGraphSimulation.SimulationRate

**Framework**: Compute Graph  
**Kind**: struct

Specifies the rate and mode for simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
struct SimulationRate
```

## Topics

### Initializers
- [init()](computegraphsimulation/simulationrate-swift.struct/init.md)
  Initializes a SimulationRate structure using default values.
### Instance Properties
- [var frequency: Float](computegraphsimulation/simulationrate-swift.struct/frequency.md)
  The number of simulation steps per second, used when [`mode`](computegraphsimulation/simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedFrequency`](computegraphsimulation/simulationrate-swift.struct/mode-swift.enum/fixedfrequency.md).
- [var mode: ComputeGraphSimulation.SimulationRate.Mode](computegraphsimulation/simulationrate-swift.struct/mode-swift.property.md)
  The simulation mode that determines how time steps are calculated.
- [var timeDelta: Float](computegraphsimulation/simulationrate-swift.struct/timedelta.md)
  The fixed time interval in seconds between simulation steps, used when [`mode`](computegraphsimulation/simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedTime`](computegraphsimulation/simulationrate-swift.struct/mode-swift.enum/fixedtime.md).
### Type Properties
- [static var `default`: ComputeGraphSimulation.SimulationRate](computegraphsimulation/simulationrate-swift.struct/default.md)
### Enumerations
- [ComputeGraphSimulation.SimulationRate.Mode](computegraphsimulation/simulationrate-swift.struct/mode-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/simulationrate-swift.struct)*