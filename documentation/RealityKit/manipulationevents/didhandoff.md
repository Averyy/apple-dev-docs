# ManipulationEvents.DidHandOff

**Framework**: RealityKit  
**Kind**: struct

An event triggered when the object is directly handed off from one hand to another

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DidHandOff
```

## Topics

### Instance Properties
- [let entity: Entity](manipulationevents/didhandoff/entity.md)
  The component’s entity.
- [let newInputDeviceSet: ManipulationEvents.InputDeviceSet](manipulationevents/didhandoff/newinputdeviceset.md)
  The input devices that the object is handed off to.
- [let oldInputDeviceSet: ManipulationEvents.InputDeviceSet](manipulationevents/didhandoff/oldinputdeviceset.md)
  The set of input devices active before handoff was initiated.

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
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  A event triggered when an entity was released.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  An event triggered when the object has reached its destination and will no longer be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/didhandoff)*