# subscribe(to:on:componentType:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)? = nil, componentType: (any Component.Type)?, _ handler: @escaping (E) -> Void) -> any Cancellable where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to.   For example   or  .
- `sourceObject`: An optional source for the event, such as an entity or a scene.   Set to   to listen for all events of the event type within the  .
- `componentType`: An optional component type to filter events to if the event is of the type  .   Set to   to listen for all events of the event type within the  .
- `handler`: A closure that runs when the   occurs.

## See Also

- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](scene/publisher(for:on:).md)
  Generates a publisher for events of the specified type.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](scene/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func publisher(for:on:componentType:)](scene/publisher(for:on:componenttype:).md)
  Returns a `Publisher` for events of the specified type in a `Scene`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/subscribe(to:on:componenttype:_:))*