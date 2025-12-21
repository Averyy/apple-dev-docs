# ManipulationEvents.DidHandOff

**Framework**: RealityKit  
**Kind**: struct

The event that occurs during a manipulation gesture when someone passes an entity from one hand to the other.

**Availability**:
- visionOS 26.0+

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
  The event that occurs when someone is about to start an entity manipulation gesture.
- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
  The event that occurs repeatedly when the entity’s transform updates during a manipulation gesture.
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  The event that occurs just as someone releases an entity during a manipulation gesture.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  The event that occurs at the end of a manipulation gesture, when the entity has reached its resting position, destination and the system no longer updates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/didhandoff)*