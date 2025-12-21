# ImagePresentationEvents.TransitionStarted

**Framework**: RealityKit  
**Kind**: struct

A transition between two viewing modes has started for an image presentation component.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct TransitionStarted
```

#### Overview

Note that a `TransitionStarted` event is not triggered for viewing mode changes that transition immediately to the new mode. For instantaneous transitions, only a `TransitionCompleted` event is fired.

Use the `TransitionStarted` event as an opportunity to hide overlaid UI during an animated transition. Update the content and location of that UI after the transition completes via a corresponding `TransitionCompleted` event.

## Topics

### Instance Properties
- [let currentViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationevents/transitionstarted/currentviewingmode.md)
  The viewing mode the image presentation component is transitioning from.
- [let targetViewingMode: ImagePresentationComponent.ViewingMode](imagepresentationevents/transitionstarted/targetviewingmode.md)
  The viewing mode the image presentation component is transitioning to.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImagePresentationEvents.TransitionCompleted](imagepresentationevents/transitioncompleted.md)
  A transition between two viewing modes has completed for an image presentation component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationevents/transitionstarted)*