# SceneEvents.TrackingStateUpdate

**Framework**: RealityKit  
**Kind**: struct

Event that triggers on a change of device tracking state

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct TrackingStateUpdate
```

## Topics

### Instance Properties
- [let current: SceneEvents.TrackingStateUpdate.State](sceneevents/trackingstateupdate/current.md)
  current tracking state of the device
- [let previous: SceneEvents.TrackingStateUpdate.State](sceneevents/trackingstateupdate/previous.md)
  previous tracking state of the device
### Enumerations
- [SceneEvents.TrackingStateUpdate.State](sceneevents/trackingstateupdate/state.md)

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SceneEvents.Update](sceneevents/update.md)
  An event invoked once per frame interval that you can use to execute custom logic for each frame.
- [SceneEvents.AnchoredStateChanged](sceneevents/anchoredstatechanged.md)
  An event invoked when the anchored state of an anchoring entity changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/trackingstateupdate)*