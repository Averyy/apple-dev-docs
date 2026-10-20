# deltaTime

**Framework**: Compute Graph  
**Kind**: property  
**Role**: Instance Property

The time interval, in seconds, to advance the simulation.

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
var deltaTime: Float
```

#### Discussion

When [`mode`](../simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedFrequency`](../simulationrate-swift.struct/mode-swift.enum/fixedfrequency.md) or [`ComputeGraphSimulation.SimulationRate.Mode.fixedTime`](../simulationrate-swift.struct/mode-swift.enum/fixedtime.md), the simulation takes between zero and [`maxSteps`](./maxsteps.md) fixed-size steps to consume this interval. Any remaining time is accumulated and carried into the next advance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advanceparams/deltatime)*