# timingMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The timing mode used to execute an action.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var timingMode: SCNActionTimingMode { get set }
```

```objc
@property (nonatomic) SCNActionTimingMode timingMode;
```

#### Discussion

For possible values, see [`SCNActionTimingMode`](../scnactiontimingmode.md). The default value is [`SCNActionTimingMode.linear`](../scnactiontimingmode/linear.md).

## See Also

### Adjusting an Action’s Animation Properties
- [var duration: TimeInterval](./duration.md)
  The duration required to complete an action.
- [var speed: CGFloat](./speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingFunction: SCNActionTimingFunction?](./timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/timingmode)*