# deltaTime

**Framework**: Compute Graph  
**Kind**: property

The time interval, in seconds, to advance the simulation.

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
var deltaTime: Float
```

#### Discussion

When [`mode`](computegraphsimulation/simulationrate-swift.struct/mode-swift.property.md) is [`ComputeGraphSimulation.SimulationRate.Mode.fixedFrequency`](computegraphsimulation/simulationrate-swift.struct/mode-swift.enum/fixedfrequency.md) or [`ComputeGraphSimulation.SimulationRate.Mode.fixedTime`](computegraphsimulation/simulationrate-swift.struct/mode-swift.enum/fixedtime.md), the simulation takes between zero and [`maxSteps`](computegraphsimulation/advanceparams/maxsteps.md) fixed-size steps to consume this interval. Any remaining time is accumulated and carried into the next advance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advanceparams/deltatime)*