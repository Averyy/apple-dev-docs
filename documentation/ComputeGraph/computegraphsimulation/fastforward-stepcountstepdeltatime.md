# fastForward(stepCount:stepDeltaTime:)

**Framework**: Compute Graph  
**Kind**: method

Advances the particle simulation by multiple steps in a single operation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func fastForward(stepCount: Int, stepDeltaTime: Float)
```

#### Discussion

This method performs batch simulation updates by executing multiple simulation steps consecutively within a single compute command buffer, skipping any non-simulation work such as updating the output buffers. This is useful for:

> **Note**: The simulation will be advanced by a total time of `stepCount * stepDeltaTime` seconds.

## Parameters

- `stepCount`: The number of simulation steps to execute. Each step represents one iteration of the simulation update cycle. Must be positive.
- `stepDeltaTime`: The time interval (in seconds) to use for each simulation step. This controls how much simulated time passes with each step. Smaller values provide more accurate simulation at the cost of requiring more steps to advance the same amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/fastforward(stepcount:stepdeltatime:))*