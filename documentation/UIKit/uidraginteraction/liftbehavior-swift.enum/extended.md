# UIDragInteraction.LiftBehavior.extended

**Framework**: UIKit  
**Kind**: case

An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case extended
```

## See Also

- [UIDragInteraction.LiftBehavior.default](uidraginteraction/liftbehavior-swift.enum/default.md)
  The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/extended)*