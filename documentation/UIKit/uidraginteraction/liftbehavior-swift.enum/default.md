# UIDragInteraction.LiftBehavior.default

**Framework**: UIKit  
**Kind**: case

The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case `default`
```

## See Also

- [UIDragInteraction.LiftBehavior.extended](uidraginteraction/liftbehavior-swift.enum/extended.md)
  An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/default)*