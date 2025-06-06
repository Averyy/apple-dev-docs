# RealityViewContentProtocol Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func add(Entity)](realityviewcameracontent/add(_:).md)
  Adds an entity to this content.
- [func remove(Entity)](realityviewcameracontent/remove(_:).md)
  Removes an entity from this content, if present.
- [func subscribe<E>(to: E.Type, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityviewcameracontent/subscribe(to:componenttype:_:).md)
  Subscribes to an event type, optionally limited to a specific component type for component events.
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, (E) -> Void) -> EventSubscription](realityviewcameracontent/subscribe(to:on:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcameracontent/realityviewcontentprotocol-implementations)*