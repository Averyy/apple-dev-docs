# ComputeGraphSimulation.SimulationRate

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Specifies the rate and mode for simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct SimulationRate
```

## Topics

### Initializers
- [init()](./simulationrate-swift.struct/init%28%29.md)
  Initializes a SimulationRate structure using default values.
### Instance Properties
- [var frequency: Float](./simulationrate-swift.struct/frequency.md)
  The number of simulation steps per second, used when [`mode`](./simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedFrequency`](./simulationrate-swift.struct/mode-swift.enum/fixedfrequency.md).
- [var mode: ComputeGraphSimulation.SimulationRate.Mode](./simulationrate-swift.struct/mode-swift.property.md)
  The simulation mode that determines how time steps are calculated.
- [var timeDelta: Float](./simulationrate-swift.struct/timedelta.md)
  The fixed time interval in seconds between simulation steps, used when [`mode`](./simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedTime`](./simulationrate-swift.struct/mode-swift.enum/fixedtime.md).
### Type Properties
- [static var `default`: ComputeGraphSimulation.SimulationRate](./simulationrate-swift.struct/default.md)
### Enumerations
- [ComputeGraphSimulation.SimulationRate.Mode](./simulationrate-swift.struct/mode-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Running a simulation
- [class ComputeGraphSimulation](../computegraphsimulation.md)
  A simulation of particles, which use a single pipeline.
- [struct ElementSpawnParameters](../elementspawnparameters.md)
  Parameters used to configure the initial state of a particle when it’s spawned in the simulation.
- [enum ElementGrouping](../elementgrouping.md)
  An enumeration of how elements are grouped.
- [enum Sorting](../sorting.md)
  An enumeration of sorting modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/simulationrate-swift.struct)*