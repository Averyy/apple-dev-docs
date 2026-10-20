# duration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The duration required to complete an action.

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
var duration: TimeInterval { get set }
```

```objc
@property (nonatomic) NSTimeInterval duration;
```

#### Discussion

This is the expected duration of an action’s animation. The actual time an action takes to complete is modified by the action’s [`timingMode`](./timingmode.md) property.

## See Also

### Adjusting an Action’s Animation Properties
- [var speed: CGFloat](./speed.md)
  A speed factor that modifies how fast an action runs.
- [var timingMode: SCNActionTimingMode](./timingmode.md)
  The timing mode used to execute an action.
- [var timingFunction: SCNActionTimingFunction?](./timingfunction.md)
  A block SceneKit calls to determine the action’s animation timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/duration)*