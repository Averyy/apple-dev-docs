# timingFunction

**Framework**: SceneKit  
**Kind**: property

A block SceneKit calls to determine the action’s animation timing.

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
var timingFunction: SCNActionTimingFunction? { get set }
```

#### Discussion

The [`timingMode`](scnaction/timingmode.md) property determines the input to your block. You use this input to compute your custom timing function, whose output determines the animation timing. The following example provides quadratic animation timing for an action, simulating the effect of gravity on a falling object:

```objc
action.timingMode = SCNActionTimingModeLinear;
action.timingFunction = ^float(float time) {
    return 1.0 - time*time;
};
```

## See Also

- [var duration: TimeInterval](scnaction/duration.md)
  The duration required to complete an action.
- [var speed: CGFloat](scnaction/speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingMode: SCNActionTimingMode](scnaction/timingmode.md)
  The timing mode used to execute an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/timingfunction)*