# speed

**Framework**: SceneKit  
**Kind**: property

A speed factor that modifies how fast an action runs.

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
var speed: CGFloat { get set }
```

#### Discussion

The speed factor adjusts how fast an action’s animation runs. For example, a speed factor of `2.0` means the animation runs twice as fast.

## See Also

- [var duration: TimeInterval](scnaction/duration.md)
  The duration required to complete an action.
- [var timingMode: SCNActionTimingMode](scnaction/timingmode.md)
  The timing mode used to execute an action.
- [var timingFunction: SCNActionTimingFunction?](scnaction/timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/speed)*