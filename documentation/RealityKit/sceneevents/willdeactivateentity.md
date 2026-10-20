# SceneEvents.WillDeactivateEntity

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Raised before an entity becomes inactive.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct WillDeactivateEntity
```

## Topics

### Instance Properties
- [let entity: Entity](./willdeactivateentity/entity.md)

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
- [SceneEvents.DidActivateEntity](./didactivateentity.md)
  Raised after an entity becomes active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/willdeactivateentity)*