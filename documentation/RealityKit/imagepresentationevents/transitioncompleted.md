# ImagePresentationEvents.TransitionCompleted

**Framework**: RealityKit  
**Kind**: struct

A transition between two viewing modes has completed for an image presentation component.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct TransitionCompleted
```

#### Overview

Use the `TransitionCompleted` event as an opportunity to display or relocate overlaid UI after a viewing mode transition.

## Topics

### Instance Properties
- [let currentViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationevents/transitioncompleted/currentviewingmode.md)
  The viewing mode the image presentation component transitioned to.
- [let previousViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationevents/transitioncompleted/previousviewingmode.md)
  The viewing mode the image presentation component transitioned from.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImagePresentationEvents.TransitionStarted](imagepresentationevents/transitionstarted.md)
  A transition between two viewing modes has started for an image presentation component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationevents/transitioncompleted)*