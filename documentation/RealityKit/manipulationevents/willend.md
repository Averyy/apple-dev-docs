# ManipulationEvents.WillEnd

**Framework**: RealityKit  
**Kind**: struct

An event triggered when the object has reached its destination and will no longer be updated.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct WillEnd
```

## Topics

### Instance Properties
- [let entity: Entity](manipulationevents/willend/entity.md)
  The component’s entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ManipulationEvents.WillBegin](manipulationevents/willbegin.md)
  A event triggered when an interaction is about to begin on a `ManipulationComponent`’s entity.
- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
  An event triggered when an entity’s transform was updated during a `ManipulationComponent`.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  An event triggered when the object is directly handed off from one hand to another
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  A event triggered when an entity was released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/willend)*