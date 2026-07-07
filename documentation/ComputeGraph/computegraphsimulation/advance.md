# advance(_:)

**Framework**: Compute Graph  
**Kind**: method

Advances the simulation by one time step, encoding all simulation stage dispatches into the command buffer and encoder provided by `params`.

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
final func advance(_ params: ComputeGraphSimulation.AdvanceParams)
```

#### Discussion

Call this once per frame from your render loop. The simulation reads [`deltaTime`](computegraphsimulation/advanceparams/deltatime.md) to determine how much simulated time to consume, subject to [`simulationRate`](computegraphsimulation/simulationrate-swift.property.md). Spatial transforms and optional viewer information in `params` are forwarded to the simulation graph.

## Parameters

- `params`: The advance parameters, including the time delta, command buffer, compute encoder, and spatial transforms for this frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/advance(_:))*