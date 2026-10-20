# publisher(for:on:componentType:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns a `Publisher` for events of the specified type in a `Scene`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func publisher<E>(for event: E.Type, on sourceObject: (any EventSource)? = nil, componentType: (any Component.Type)?) -> Scene.Publisher<E> where E : Event
```

#### Return Value

A `Publisher` for events of the specified type.

## Parameters

- `event`: The event type to subscribe to. For example, [`SceneEvents.Update`](../sceneevents/update.md).
- `sourceObject`: The event source – usually the entity you are interested in. `nil` to listen all events of this type that occur in the scene.
- `componentType`: The component type, or `nil` for all (for ComponentEvents).

## See Also

### Publishing and subscribing to events
- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](./publisher%28for,on%29.md)
  Generates a publisher for events of the specified type.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](./subscribe%28to,on,_%29.md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> any Cancellable](./subscribe%28to,on,componenttype,_%29.md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher(for:on:componenttype:))*