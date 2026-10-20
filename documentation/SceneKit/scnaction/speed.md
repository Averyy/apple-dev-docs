# speed

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A speed factor that modifies how fast an action runs.

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
var speed: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat speed;
```

#### Discussion

The speed factor adjusts how fast an action’s animation runs. For example, a speed factor of `2.0` means the animation runs twice as fast.

## See Also

### Adjusting an Action’s Animation Properties
- [var duration: TimeInterval](./duration.md)
  The duration required to complete an action.
- [var timingMode: SCNActionTimingMode](./timingmode.md)
  The timing mode used to execute an action.
- [var timingFunction: SCNActionTimingFunction?](./timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/speed)*