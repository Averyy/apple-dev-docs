# AnimationEvents.RootMotionDidUpdate

**Framework**: RealityKit  
**Kind**: struct

Fired each frame when the animation graph produces a root motion delta for an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RootMotionDidUpdate
```

#### Overview

By default, subscribing to this event suppresses automatic application of the root motion delta. The subscriber is then fully responsible for applying or discarding it.

To observe root motion without taking over application, set [`suppressesAutomaticApplication`](animationevents/rootmotiondidupdate/suppressesautomaticapplication.md) to `false` inside the handler:

```swift
scene.subscribe(to: AnimationEvents.RootMotionDidUpdate.self, on: entity) { event in
    event.suppressesAutomaticApplication = false
    // Root motion is still applied automatically; use the event for observation only.
    print("Delta: \(event.rootMotionTransform)")
}
```

To fully control application, leave the default (`true`) and apply the transform yourself:

```swift
scene.subscribe(to: AnimationEvents.RootMotionDidUpdate.self, on: entity) { event in
    entity.transform = event.rootMotionTransform * entity.transform
}
```

The event fires after graph evaluation but before the skeletal pose is applied to the mesh.

## Topics

### Accessing root motion
- [let rootMotionTransform: Transform](animationevents/rootmotiondidupdate/rootmotiontransform.md)
  The change in position and orientation since the previous frame.
- [var suppressesAutomaticApplication: Bool](animationevents/rootmotiondidupdate/suppressesautomaticapplication.md)
  Controls whether subscribing suppresses automatic root motion application.
### Instance Properties
- [let deltaTime: TimeInterval](animationevents/rootmotiondidupdate/deltatime.md)
  The elapsed time since the last update.
- [let entity: Entity](animationevents/rootmotiondidupdate/entity.md)
  The entity being animated.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate)*