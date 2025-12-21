# ManipulationEvents.DidUpdateTransform

**Framework**: RealityKit  
**Kind**: struct

The event that occurs repeatedly when the entity’s transform updates during a manipulation gesture.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DidUpdateTransform
```

## Topics

### Instance Properties
- [let entity: Entity](manipulationevents/didupdatetransform/entity.md)
  The component’s entity.
- [let inputDeviceSet: ManipulationEvents.InputDeviceSet](manipulationevents/didupdatetransform/inputdeviceset.md)
  The active set of `InputDevice`s on the entity.
- [let pivotPoint: Point3DFloat](manipulationevents/didupdatetransform/pivotpoint.md)
  This point is in the coordinate space of `entity`

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ManipulationEvents.WillBegin](manipulationevents/willbegin.md)
  The event that occurs when someone is about to start an entity manipulation gesture.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  The event that occurs during a manipulation gesture when someone passes an entity from one hand to the other.
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  The event that occurs just as someone releases an entity during a manipulation gesture.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  The event that occurs at the end of a manipulation gesture, when the entity has reached its resting position, destination and the system no longer updates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/didupdatetransform)*