# liftBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that controls the timing behavior for initiating a drag gesture from a touch.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
var liftBehavior: UIDragInteraction.LiftBehavior { get set }
```

```objc
@property (nonatomic, assign) UIDragLiftBehavior liftBehavior;
```

#### Discussion

The default value is [`UIDragInteraction.LiftBehavior.default`](./liftbehavior-swift.enum/default.md), which uses the standard lift timing parameters.

Set this property to [`UIDragInteraction.LiftBehavior.extended`](./liftbehavior-swift.enum/extended.md) in gesture-rich views where recognizers compete for the same touches. The extended behavior increases the lift delay and cancels the drag when a second touch is detected, allowing other long-press gestures on the same view to activate before the drag begins.

For pointer-initiated drags, use [`allowsPointerDragBeforeLiftDelay`](./allowspointerdragbeforeliftdelay.md) to control whether pointer drags respect the lift delay independently of this property.

## See Also

### Configuring lift behavior
- [UIDragInteraction.LiftBehavior](./liftbehavior-swift.enum.md)
  Constants that determine the lift behavior for a drag interaction.
- [var allowsPointerDragBeforeLiftDelay: Bool](./allowspointerdragbeforeliftdelay.md)
  A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.property)*