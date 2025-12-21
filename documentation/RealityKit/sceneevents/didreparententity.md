# SceneEvents.DidReparentEntity

**Framework**: RealityKit  
**Kind**: struct

Raised after an entity has been reparented within the same scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct DidReparentEntity
```

## Topics

### Instance Properties
- [let child: Entity](sceneevents/didreparententity/child.md)
- [let previousParent: Entity?](sceneevents/didreparententity/previousparent.md)

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SceneEvents.DidAddEntity](sceneevents/didaddentity.md)
  Raised after an entity is added to the scene.
- [SceneEvents.WillRemoveEntity](sceneevents/willremoveentity.md)
  Raised before an entity is removed from the scene.
- [SceneEvents.DidActivateEntity](sceneevents/didactivateentity.md)
  Raised after an entity becomes active.
- [SceneEvents.WillDeactivateEntity](sceneevents/willdeactivateentity.md)
  Raised before an entity becomes inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/didreparententity)*