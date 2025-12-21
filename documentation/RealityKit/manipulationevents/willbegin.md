# ManipulationEvents.WillBegin

**Framework**: RealityKit  
**Kind**: struct

The event that occurs when someone is about to start an entity manipulation gesture.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct WillBegin
```

## Topics

### Instance Properties
- [let entity: Entity](manipulationevents/willbegin/entity.md)
  The component’s entity.
- [let inputDeviceSet: ManipulationEvents.InputDeviceSet](manipulationevents/willbegin/inputdeviceset.md)
  The input element that triggered the interaction.
- [let pivotPoint: Point3DFloat](manipulationevents/willbegin/pivotpoint.md)
  This point is in the coordinate space configured in the view modifier.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
  The event that occurs repeatedly when the entity’s transform updates during a manipulation gesture.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  The event that occurs during a manipulation gesture when someone passes an entity from one hand to the other.
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  The event that occurs just as someone releases an entity during a manipulation gesture.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  The event that occurs at the end of a manipulation gesture, when the entity has reached its resting position, destination and the system no longer updates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/willbegin)*