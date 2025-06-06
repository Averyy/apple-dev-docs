# ComponentEvents

**Framework**: RealityKit  
**Kind**: enum

Provides the events related to components.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum ComponentEvents
```

#### Overview

For more information on subscribing to scene events, see `RealityKit/Scene/Event`.

## Topics

### Detecting component changes
- [ComponentEvents.DidAdd](componentevents/didadd.md)
  Event raised after a component has been added to an entity,
- [ComponentEvents.DidChange](componentevents/didchange.md)
  Event raised after a component has been modified.
- [ComponentEvents.WillRemove](componentevents/willremove.md)
  Event raised before a component is removed from an entity.
### Detecting component activations
- [ComponentEvents.DidActivate](componentevents/didactivate.md)
  Event raised after a component has been activated.
- [ComponentEvents.WillDeactivate](componentevents/willdeactivate.md)
  Event raised before a component is deactivated.

## See Also

- [protocol Event](event.md)
  A type that can be sent as an event.
- [protocol EventSource](eventsource.md)
  A type on which events can be published and subscribed.
- [struct EventSubscription](eventsubscription.md)
  A subscription to an event.
- [enum SceneEvents](sceneevents.md)
  Events the scene invokes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentevents)*