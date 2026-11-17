# Scene.Publisher

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A publisher for the given event type in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Publisher<E> where E : Event
```

## Relationships

### Conforms To
- [Publisher](../../Combine/publisher.md)

## See Also

### Event publishers and subscription
- [enum SceneEvents](../sceneevents.md)
  Events the scene invokes.
- [func storeWhileEntityActive(Entity)](../../Combine/cancellable/storewhileentityactive%28_%29.md)
  Retains the `Cancellable` as long as the entity is active (see `Entity.isActive`). If the entity is deactivated, the `Cancellable` is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher)*