# publisher(for:on:)

**Framework**: RealityKit  
**Kind**: method

Generates a publisher for events of the specified type.

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
@preconcurrency func publisher<E>(for event: E.Type, on sourceObject: (any EventSource)? = nil) -> Scene.Publisher<E> where E : Event
```

#### Return Value

A publisher for events of the specified type.

## Parameters

- `event`: The event, like  .
- `sourceObject`: The source of the event. Set to   to publish all   events of the given type within the scene.

## See Also

- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> any Cancellable](scene/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func publisher(for:on:componentType:)](scene/publisher(for:on:componenttype:).md)
  Returns a `Publisher` for events of the specified type in a `Scene`.
- [func subscribe(to:on:componentType:_:)](scene/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher(for:on:))*