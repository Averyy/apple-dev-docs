# duration

**Framework**: SceneKit  
**Kind**: property

The duration required to complete an action.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var duration: TimeInterval { get set }
```

#### Discussion

This is the expected duration of an action’s animation. The actual time an action takes to complete is modified by the action’s [`timingMode`](scnaction/timingmode.md) property.

## See Also

- [var speed: CGFloat](scnaction/speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingMode: SCNActionTimingMode](scnaction/timingmode.md)
  The timing mode used to execute an action.
- [var timingFunction: SCNActionTimingFunction?](scnaction/timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/duration)*