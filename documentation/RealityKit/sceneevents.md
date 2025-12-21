# SceneEvents

**Framework**: RealityKit  
**Kind**: enum

Events the scene invokes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
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
- [SceneEvents.TrackingStateUpdate](sceneevents/trackingstateupdate.md)
  Event that triggers on a change of device tracking state
### Detecting scene hierarchy changes
- [SceneEvents.DidAddEntity](sceneevents/didaddentity.md)
  Raised after an entity is added to the scene.
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity.md)
  Raised after an entity has been reparented within the same scene.
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity.md)
  Raised before an entity is removed from the scene.
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity.md)
  Raised after an entity becomes active.
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity.md)
  Raised before an entity becomes inactive.

## See Also

- [enum AnchorStateEvents](anchorstateevents.md)
  Events that trigger on an entity to indicate a change in anchor state.
- [enum ComponentEvents](componentevents.md)
  Provides the events related to components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents)*