# UIDragInteraction.LiftBehavior.default

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
case `default`
```

```c
UIDragLiftBehaviorDefault
```

## See Also

### Lift behaviors
- [UIDragInteraction.LiftBehavior.extended](./extended.md)
  An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/default)*