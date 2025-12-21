# SceneEvents.AnchoredStateChanged

**Framework**: RealityKit  
**Kind**: struct

An event invoked when the anchored state of an anchoring entity changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct AnchoredStateChanged
```

## Topics

### Characterizing an update
- [let anchor: any HasAnchoring](sceneevents/anchoredstatechanged/anchor.md)
  The entity whose anchoring state changed.
- [let isAnchored: Bool](sceneevents/anchoredstatechanged/isanchored.md)
  The current anchoring state of the entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SceneEvents.Update](sceneevents/update.md)
  An event invoked once per frame interval that you can use to execute custom logic for each frame.
- [SceneEvents.TrackingStateUpdate](sceneevents/trackingstateupdate.md)
  Event that triggers on a change of device tracking state


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/anchoredstatechanged)*