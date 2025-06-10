# publisher(for:on:componentType:)

**Framework**: RealityKit  
**Kind**: method

Returns a `Publisher` for events of the specified type in a `Scene`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func publisher<E>(for event: E.Type, on sourceObject: (any EventSource)? = nil, componentType: (any Component.Type)?) -> Scene.Publisher<E> where E : Event
```

#### Return Value

A `Publisher` for events of the specified type.

## Parameters

- `event`: The event type to subscribe to. For example,  .
- `sourceObject`: The event source – usually the entity you are interested in.   to   listen all events of this type that occur in the scene.
- `componentType`: The component type, or   for all (for ComponentEvents).

## See Also

- [func publisher<E>(for: E.Type, on: (any EventSource)?) -> Scene.Publisher<E>](scene/publisher(for:on:).md)
  Generates a publisher for events of the specified type.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](scene/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func subscribe(to:on:componentType:_:)](scene/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher(for:on:componenttype:))*