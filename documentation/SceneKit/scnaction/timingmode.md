# timingMode

**Framework**: SceneKit  
**Kind**: property

The timing mode used to execute an action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var timingMode: SCNActionTimingMode { get set }
```

#### Discussion

For possible values, see [`SCNActionTimingMode`](scnactiontimingmode.md). The default value is [`SCNActionTimingMode.linear`](scnactiontimingmode/linear.md).

## See Also

- [var duration: TimeInterval](scnaction/duration.md)
  The duration required to complete an action.
- [var speed: CGFloat](scnaction/speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingFunction: SCNActionTimingFunction?](scnaction/timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/timingmode)*