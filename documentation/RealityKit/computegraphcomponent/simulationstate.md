# ComputeGraphComponent.SimulationState

**Framework**: RealityKit  
**Kind**: enum

The playback state of a compute graph simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SimulationState
```

## Topics

### Enumeration Cases
- [ComputeGraphComponent.SimulationState.paused](computegraphcomponent/simulationstate/paused.md)
  The simulation is frozen; no steps are evaluated.
- [ComputeGraphComponent.SimulationState.playing](computegraphcomponent/simulationstate/playing.md)
  The simulation advances each frame at its configured rate.
- [ComputeGraphComponent.SimulationState.stepping](computegraphcomponent/simulationstate/stepping.md)
  The simulation evaluates exactly one step on the next frame, then returns to [`ComputeGraphComponent.SimulationState.paused`](computegraphcomponent/simulationstate/paused.md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/simulationstate)*