# UIDragInteraction.LiftBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine the lift behavior for a drag interaction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
enum LiftBehavior
```

```c
enum UIDragLiftBehavior : NSUInteger;
```

## Topics

### Lift behaviors
- [UIDragInteraction.LiftBehavior.default](./liftbehavior-swift.enum/default.md)
  The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.
- [UIDragInteraction.LiftBehavior.extended](./liftbehavior-swift.enum/extended.md)
  An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.
### Initializers
- [init?(rawValue: UInt)](./liftbehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring lift behavior
- [var liftBehavior: UIDragInteraction.LiftBehavior](./liftbehavior-swift.property.md)
  A value that controls the timing behavior for initiating a drag gesture from a touch.
- [var allowsPointerDragBeforeLiftDelay: Bool](./allowspointerdragbeforeliftdelay.md)
  A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum)*