# SceneEvents.Update

**Framework**: RealityKit  
**Kind**: struct

An event invoked once per frame interval that you can use to execute custom logic for each frame.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct Update
```

## Topics

### Characterizing an update
- [let scene: Scene](sceneevents/update/scene.md)
  The updated scene.
- [let deltaTime: TimeInterval](sceneevents/update/deltatime.md)
  The elapsed time since the last update.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SceneEvents.AnchoredStateChanged](sceneevents/anchoredstatechanged.md)
  An event invoked when the anchored state of an anchoring entity changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sceneevents/update)*