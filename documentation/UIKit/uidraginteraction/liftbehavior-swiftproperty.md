# liftBehavior

**Framework**: UIKit  
**Kind**: property

A value that controls the timing behavior for initiating a drag gesture from a touch.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var liftBehavior: UIDragInteraction.LiftBehavior { get set }
```

#### Discussion

The default value is [`UIDragInteraction.LiftBehavior.default`](uidraginteraction/liftbehavior-swift.enum/default.md), which uses the standard lift timing parameters.

Set this property to [`UIDragInteraction.LiftBehavior.extended`](uidraginteraction/liftbehavior-swift.enum/extended.md) in gesture-rich views where recognizers compete for the same touches. The extended behavior increases the lift delay and cancels the drag when a second touch is detected, allowing other long-press gestures on the same view to activate before the drag begins.

For pointer-initiated drags, use [`allowsPointerDragBeforeLiftDelay`](uidraginteraction/allowspointerdragbeforeliftdelay.md) to control whether pointer drags respect the lift delay independently of this property.

## See Also

- [UIDragInteraction.LiftBehavior](uidraginteraction/liftbehavior-swift.enum.md)
  Constants that determine the lift behavior for a drag interaction.
- [var allowsPointerDragBeforeLiftDelay: Bool](uidraginteraction/allowspointerdragbeforeliftdelay.md)
  A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.property)*