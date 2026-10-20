# SceneEvents.DidActivateEntity

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Raised after an entity becomes active.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct DidActivateEntity
```

## Topics

### Instance Properties
- [let entity: Entity](./didactivateentity/entity.md)

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting scene hierarchy changes
- [SceneEvents.DidAddEntity](./didaddentity.md)
  Raised after an entity is added to the scene.
- [SceneEvents.DidReparentEntity](./didreparententity.md)
  Raised after an entity has been reparented within the same scene.
- [SceneEvents.WillRemoveEntity](./willremoveentity.md)
  Raised before an entity is removed from the scene.
- [SceneEvents.WillDeactivateEntity](./willdeactivateentity.md)
  Raised before an entity becomes inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/didactivateentity)*