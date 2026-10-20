# ComputeGraphComponent.SimulationState

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The playback state of a compute graph simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum SimulationState
```

## Topics

### Enumeration Cases
- [ComputeGraphComponent.SimulationState.paused](./simulationstate/paused.md)
  The simulation is frozen; no steps are evaluated.
- [ComputeGraphComponent.SimulationState.playing](./simulationstate/playing.md)
  The simulation advances each frame at its configured rate.
- [ComputeGraphComponent.SimulationState.stepping](./simulationstate/stepping.md)
  The simulation advances a single frame, then returns to [`ComputeGraphComponent.SimulationState.paused`](./simulationstate/paused.md).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/simulationstate)*