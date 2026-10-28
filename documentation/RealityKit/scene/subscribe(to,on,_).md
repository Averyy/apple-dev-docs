# subscribe(to:on:_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Subscribes to an event type, optionally limited to events affecting a source entity or scene.

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
@preconcurrency func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)? = nil, _ handler: @escaping (E) -> Void) -> any Cancellable where E : Event
```

## Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to. For example [`SceneEvents.Update`](../sceneevents/update.md) or [`ComponentEvents.DidAdd`](../componentevents/didadd.md).
- `sourceObject`: An optional source for the event, such as an entity or a scene. Set to `nil` to listen for all events of the event type within the [`Scene`](../scene.md).
- `handler`: A closure that runs when the `event` occurs.

## See Also

### Publishing and subscribing to events
- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](./publisher%28for,on%29.md)
  Generates a publisher for events of the specified type.
- [func publisher<E>(for: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?) -> Scene.Publisher<E>](./publisher%28for,on,componenttype%29.md)
  Returns a `Publisher` for events of the specified type in a `Scene`.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> any Cancellable](./subscribe%28to,on,componenttype,_%29.md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/subscribe(to:on:_:))*