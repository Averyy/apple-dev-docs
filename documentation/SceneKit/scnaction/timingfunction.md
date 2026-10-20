# timingFunction

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A block SceneKit calls to determine the action’s animation timing.

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
var timingFunction: SCNActionTimingFunction? { get set }
```

```objc
@property (nonatomic, nullable) SCNActionTimingFunction timingFunction;
```

#### Discussion

The [`timingMode`](./timingmode.md) property determines the input to your block. You use this input to compute your custom timing function, whose output determines the animation timing. The following example provides quadratic animation timing for an action, simulating the effect of gravity on a falling object:

```objc
action.timingMode = SCNActionTimingModeLinear;
action.timingFunction = ^float(float time) {
    return 1.0 - time*time;
};
```

## See Also

### Adjusting an Action’s Animation Properties
- [var duration: TimeInterval](./duration.md)
  The duration required to complete an action.
- [var speed: CGFloat](./speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingMode: SCNActionTimingMode](./timingmode.md)
  The timing mode used to execute an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/timingfunction)*