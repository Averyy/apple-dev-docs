# ImagePresentationEvents.TransitionCompleted

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A transition between two viewing modes has completed for an image presentation component.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct TransitionCompleted
```

#### Overview

Use the `TransitionCompleted` event as an opportunity to display or relocate overlaid UI after a viewing mode transition.

## Topics

### Instance Properties
- [let currentViewingMode: ImagePresentationComponent.ViewingMode](./transitioncompleted/currentviewingmode.md)
  The viewing mode the image presentation component transitioned to.
- [let previousViewingMode: ImagePresentationComponent.ViewingMode](./transitioncompleted/previousviewingmode.md)
  The viewing mode the image presentation component transitioned from.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Viewing mode transitions
- [ImagePresentationEvents.TransitionStarted](./transitionstarted.md)
  A transition between two viewing modes has started for an image presentation component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationevents/transitioncompleted)*