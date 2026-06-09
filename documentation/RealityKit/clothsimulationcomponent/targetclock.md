# targetClock

**Framework**: RealityKit  
**Kind**: property

The clock that this simulation attempts to follow.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var targetClock: CMClockOrTimebase { get set }
```

#### Discussion

The tempo of this clock can be adjusted to slow down or completely pause the simulation. The simulation may not be able to perfectly follow the target clock due to [`maximumStepsPerUpdate`](clothsimulationcomponent/maximumstepsperupdate-swift.property.md).

Defaults to the RealityKit engine clock.

## See Also

- [var simulationClock: CMClockOrTimebase](clothsimulationcomponent/simulationclock.md)
  The clock that tracks the pace of this simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/targetclock)*