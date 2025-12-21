# AnchorStateEvents

**Framework**: RealityKit  
**Kind**: enum

Events that trigger on an entity to indicate a change in anchor state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum AnchorStateEvents
```

#### Overview

You need to set up [`SpatialTrackingSession`](spatialtrackingsession.md) to listen for this event.

## Topics

### Structures
- [AnchorStateEvents.DidAnchor](anchorstateevents/didanchor.md)
  Event that triggers on an entity after the entity is anchored with certain reasons.
- [AnchorStateEvents.DidFailToAnchor](anchorstateevents/didfailtoanchor.md)
  Event that triggers on an entity when pending anchor encounters an error.
- [AnchorStateEvents.WillUnanchor](anchorstateevents/willunanchor.md)
  Event that triggers on an entity before the entity is unanchored with certain reasons.

## See Also

- [enum SceneEvents](sceneevents.md)
  Events the scene invokes.
- [enum ComponentEvents](componentevents.md)
  Provides the events related to components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorstateevents)*