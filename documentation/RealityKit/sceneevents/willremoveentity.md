# SceneEvents.WillRemoveEntity

**Framework**: RealityKit  
**Kind**: struct

Raised before an entity is removed from the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct WillRemoveEntity
```

## Topics

### Instance Properties
- [let entity: Entity](sceneevents/willremoveentity/entity.md)

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [SceneEvents.DidAddEntity](sceneevents/didaddentity.md)
  Raised after an entity is added to the scene.
- [SceneEvents.DidReparentEntity](sceneevents/didreparententity.md)
  Raised after an entity has been reparented within the same scene.
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity.md)
  Raised after an entity becomes active.
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity.md)
  Raised before an entity becomes inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/willremoveentity)*