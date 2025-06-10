# subscribe(to:componentType:_:)

**Framework**: RealityKit  
**Kind**: method

Subscribes to an event type, optionally limited to a specific component type for component events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
func subscribe<E>(to event: E.Type, componentType: (any Component.Type)? = nil, _ handler: @escaping (E) -> Void) -> EventSubscription where E : Event
```

#### Return Value

An object that represents the subscription to this event stream.

#### Discussion

Events you can subscribe to including scene updates, [`SceneEvents.Update`](sceneevents/update.md), or when an animation ends, [`AnimationEvents.PlaybackCompleted`](animationevents/playbackcompleted.md).

## Parameters

- `event`: The event type to subscribe to.   For example,   or  .
- `componentType`: An optional component type to filter events to if the event is of the type  .   Set to   to listen for all events of the event type within the view content.
- `handler`: A closure that runs when the   occurs.

## See Also

- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontentprotocol/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or a specific component type for component events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontentprotocol/subscribe(to:componenttype:_:))*