# subscribe(to:on:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to events affecting a source entity or scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)?, _ handler: @escaping (E) -> Void) -> EventSubscription where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to.   For example,   or  .
- `sourceObject`: An optional source for the event, such as an entity or a scene.   Set to   to listen for all events of the event type within the view content.
- `handler`: A closure that runs when the   occurs.

## See Also

- [func subscribe<E>(to: E.Type, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:componenttype:_:).md)
  Subscribes to an event type, optionally limited to a specific component type for component events.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontentprotocol/subscribe(to:on:_:))*