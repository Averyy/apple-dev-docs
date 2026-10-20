# publisher(for:on:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Generates a publisher for events of the specified type.

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
@preconcurrency func publisher<E>(for event: E.Type, on sourceObject: (any EventSource)? = nil) -> Scene.Publisher<E> where E : Event
```

#### Return Value

A publisher for events of the specified type.

## Parameters

- `event`: The event, like `SceneEvents.Update.self`.
- `sourceObject`: The source of the event. Set to `nil` to publish all events of the given type within the scene.

## See Also

### Publishing and subscribing to events
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](./subscribe%28to,on,_%29.md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func publisher<E>(for: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?) -> Scene.Publisher<E>](./publisher%28for,on,componenttype%29.md)
  Returns a `Publisher` for events of the specified type in a `Scene`.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> any Cancellable](./subscribe%28to,on,componenttype,_%29.md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher(for:on:))*