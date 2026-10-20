# AnimationEvents.RootMotionDidUpdate

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event raised each frame when a new root motion delta is produced for an entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct RootMotionDidUpdate
```

#### Overview

Root motion is locomotion that’s authored into an animation itself — for example, a run cycle whose root joint advances forward — rather than driven by code. Each frame’s contribution is reported as a [`rootMotionTransform`](./rootmotiondidupdate/rootmotiontransform.md) delta, which the system applies to the entity’s transform automatically. The event fires after animation evaluation but before the resulting skeletal pose is applied to the mesh.

Subscribe to this event when you need to take over root motion application — for example, to project the delta onto a navigation surface or to reject motion on collision. By default, subscribing through `scene.subscribe(to:on:)` suppresses the automatic application; the subscriber is then fully responsible for applying or discarding the delta.

##### Take over root motion application

```swift
scene.subscribe(to: AnimationEvents.RootMotionDidUpdate.self, on: entity) { event in
    entity.transform = event.rootMotionTransform * entity.transform
}
```

##### Observe root motion without taking over

To observe the delta while leaving automatic application in place, set [`suppressesAutomaticApplication`](./rootmotiondidupdate/suppressesautomaticapplication.md) to `false` inside the handler:

```swift
scene.subscribe(to: AnimationEvents.RootMotionDidUpdate.self, on: entity) { event in
    event.suppressesAutomaticApplication = false
    print("Delta: \(event.rootMotionTransform)")
}
```

## Topics

### Accessing root motion
- [let rootMotionTransform: Transform](./rootmotiondidupdate/rootmotiontransform.md)
  The change in position and orientation since the previous frame.
- [var suppressesAutomaticApplication: Bool](./rootmotiondidupdate/suppressesautomaticapplication.md)
  A Boolean value that controls whether subscribing to the event suppresses automatic application of the root motion delta.
### Instance Properties
- [let deltaTime: TimeInterval](./rootmotiondidupdate/deltatime.md)
  The elapsed time since the last update, in seconds.
- [let entity: Entity](./rootmotiondidupdate/entity.md)
  The entity the root motion delta was produced for.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate)*