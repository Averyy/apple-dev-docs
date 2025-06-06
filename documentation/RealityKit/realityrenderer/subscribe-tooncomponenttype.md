# subscribe(to:on:componentType:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)? = nil, componentType: (any Component.Type)? = nil, _ handler: @escaping (E) -> Void) -> EventSubscription where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to.   For example   or  .
- `sourceObject`: An optional source for the event, such as an entity or a scene.   Set to   to listen for all events of the event type within the  .
- `componentType`: An optional component type to filter events to if the event is of the type  .   Set to   to listen for all events of the event type within the  .
- `handler`: A closure that runs when the   occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/subscribe(to:on:componenttype:_:))*