# ComputeGraphSimulation.SimulationRate.Mode.fixedTime

**Framework**: ComputeGraph  
**Kind**: case

Simulate using time delta.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
case fixedTime
```

#### Discussion

Similar to fixedFrequency except the timeDelta is in seconds.

This can result in zero, one, or more steps per frame, depending on the frequency specified and the current framerate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/simulationrate-swift.struct/mode-swift.enum/fixedtime)*