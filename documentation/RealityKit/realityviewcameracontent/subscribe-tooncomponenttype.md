# subscribe(to:on:componentType:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
func subscribe<E>(to event: E.Type, on sourceObject: (any EventSource)?, componentType: (any Component.Type)?, _ handler: @escaping (E) -> Void) -> EventSubscription where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

## Parameters

- `event`: The event type to subscribe to. For example, [`SceneEvents.Update`](sceneevents/update.md) or [`ComponentEvents.DidActivate`](componentevents/didactivate.md).
- `sourceObject`: An optional source for the event, such as an entity or a scene. Set to `nil` to listen for all events of the event type within the [`RealityViewCameraContent`](realityviewcameracontent.md).
- `componentType`: An optional component type to filter events to if the event is of the type [`ComponentEvents`](componentevents.md). Set to `nil` to listen for all events of the event type within the [`RealityViewCameraContent`](realityviewcameracontent.md).
- `handler`: A closure that runs when the `event` occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/subscribe(to:on:componenttype:_:))*