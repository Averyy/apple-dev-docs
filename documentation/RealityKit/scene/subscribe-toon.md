# subscribe(to:on:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to events affecting a source entity or scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)? = nil, _ handler: @escaping (E) -> Void) -> any Cancellable where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to.   For example   or  .
- `sourceObject`: An optional source for the event, such as an entity or a scene.   Set to   to listen for all events of the event type within the  .
- `handler`: A closure that runs when the   occurs.

## See Also

- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](scene/publisher(for:on:).md)
  Generates a publisher for events of the specified type.
- [func publisher(for:on:componentType:)](scene/publisher(for:on:componenttype:).md)
  Returns a `Publisher` for events of the specified type in a `Scene`.
- [func subscribe(to:on:componentType:_:)](scene/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/subscribe(to:on:_:))*