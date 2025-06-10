# ManipulationEvents.WillRelease

**Framework**: RealityKit  
**Kind**: struct

A event triggered when an entity was released.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct WillRelease
```

## Topics

### Instance Properties
- [let entity: Entity](manipulationevents/willrelease/entity.md)
  The component’s entity.
- [let inputDeviceSet: ManipulationEvents.InputDeviceSet](manipulationevents/willrelease/inputdeviceset.md)
  The input devices that ended the interaction.
- [let wasCancelled: Bool](manipulationevents/willrelease/wascancelled.md)
  Whether the release was caused by a cancelled interaction.

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
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  An event triggered when the object has reached its destination and will no longer be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/willrelease)*