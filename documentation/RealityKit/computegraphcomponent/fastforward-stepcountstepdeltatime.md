# fastForward(stepCount:stepDeltaTime:)

**Framework**: RealityKit  
**Kind**: method

Advances the particle simulation by multiple steps in a single operation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func fastForward(stepCount: Int, stepDeltaTime: Float)
```

#### Discussion

> **Note**: The simulation will be advanced by a total time of `stepCount * stepDeltaTime` seconds.

## Parameters

- `stepCount`: The number of simulation steps to execute. Each step represents one iteration of the simulation update cycle. Must be positive.
- `stepDeltaTime`: The time interval (in seconds) to use for each simulation step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/fastforward(stepcount:stepdeltatime:))*