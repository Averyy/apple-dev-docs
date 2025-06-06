# RealityViewContentProtocol Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func add(Entity)](realityviewcontent/add(_:).md)
  Adds an entity to this content.
- [func remove(Entity)](realityviewcontent/remove(_:).md)
  Removes an entity from this content, if present.
- [func subscribe<E>(to: E.Type, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcontent/subscribe(to:componenttype:_:).md)
  Subscribes to an event type, optionally limited to a specific component type for component events.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> EventSubscription](realityviewcontent/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontent/realityviewcontentprotocol-implementations)*