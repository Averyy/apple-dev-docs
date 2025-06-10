# SceneEvents

**Framework**: RealityKit  
**Kind**: enum

Events the scene invokes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum SceneEvents
```

#### Overview

For more information on subscribing to scene events, see `RealityKit/Scene/Event`.

## Topics

### Detecting scene-level updates
- [SceneEvents.Update](sceneevents/update.md)
  An event invoked once per frame interval that you can use to execute custom logic for each frame.
- [SceneEvents.AnchoredStateChanged](sceneevents/anchoredstatechanged.md)
  An event invoked when the anchored state of an anchoring entity changes.
### Structures
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity-5jy9a.md)
  Raised after an entity becomes active.
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity-8my6.md)
  Raised after an entity becomes active.
- [SceneEvents.DidAddEntity](sceneevents/didaddentity-6yi7l.md)
  Raised after an entity is added to the scene.
- [SceneEvents.DidAddEntity](sceneevents/didaddentity-9sx4i.md)
  Raised after an entity is added to the scene.
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity-2rsns.md)
  Raised after an entity has been reparented within the same scene.
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity-8xr41.md)
  Raised after an entity has been reparented within the same scene.
- [SceneEvents.TrackingStateUpdate](sceneevents/trackingstateupdate-59q6r.md)
  Event that triggers on a change of device tracking state
- [SceneEvents.TrackingStateUpdate](sceneevents/trackingstateupdate-9q21e.md)
  Event that triggers on a change of device tracking state
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity-3mahl.md)
  Raised before an entity becomes inactive.
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity-4vvwc.md)
  Raised before an entity becomes inactive.
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity-2fca3.md)
  Raised before an entity is removed from the scene.
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity-83c6c.md)
  Raised before an entity is removed from the scene.

## See Also

- [enum AnchorStateEvents](anchorstateevents.md)
  Events that trigger on an entity to indicate a change in anchor state.
- [enum ComponentEvents](componentevents.md)
  Provides the events related to components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents)*