# simulationClock

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The clock that tracks the pace of this simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var simulationClock: CMClockOrTimebase { get }
```

#### Discussion

Syncing with this clock ensures synchronization with the simulation. For instance, an animation can be played using this clock to ensure that the motion of said animation is synchronized with the simulation.

This clock generally tries to match [`targetClock`](./targetclock.md), but the two can deviate at times. This is because the simulation may not be able to perfectly follow the target clock due to [`maximumStepsPerUpdate`](./maximumstepsperupdate-swift.property.md).

## See Also

### Synchronizing the clock
- [var targetClock: CMClockOrTimebase](./targetclock.md)
  The clock that this simulation attempts to follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/simulationclock)*