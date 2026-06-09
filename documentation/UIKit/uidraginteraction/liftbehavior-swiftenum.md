# UIDragInteraction.LiftBehavior

**Framework**: UIKit  
**Kind**: enum

Constants that determine the lift behavior for a drag interaction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum LiftBehavior
```

## Topics

### Lift behaviors
- [UIDragInteraction.LiftBehavior.default](uidraginteraction/liftbehavior-swift.enum/default.md)
  The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.
- [UIDragInteraction.LiftBehavior.extended](uidraginteraction/liftbehavior-swift.enum/extended.md)
  An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.
### Initializers
- [init?(rawValue: UInt)](uidraginteraction/liftbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var liftBehavior: UIDragInteraction.LiftBehavior](uidraginteraction/liftbehavior-swift.property.md)
  A value that controls the timing behavior for initiating a drag gesture from a touch.
- [var allowsPointerDragBeforeLiftDelay: Bool](uidraginteraction/allowspointerdragbeforeliftdelay.md)
  A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum)*