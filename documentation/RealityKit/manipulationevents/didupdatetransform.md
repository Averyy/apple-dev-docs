# ManipulationEvents.DidUpdateTransform

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event that occurs repeatedly when the entity’s transform updates during a manipulation gesture.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DidUpdateTransform
```

## Topics

### Instance Properties
- [let entity: Entity](./didupdatetransform/entity.md)
  The component’s entity.
- [let inputDeviceSet: ManipulationEvents.InputDeviceSet](./didupdatetransform/inputdeviceset.md)
  The active set of `InputDevice`s on the entity.
- [let pivotPoint: Point3DFloat](./didupdatetransform/pivotpoint.md)
  This point is in the coordinate space of `entity`

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting manipulation gesture events
- [ManipulationEvents.WillBegin](./willbegin.md)
  The event that occurs when someone is about to start an entity manipulation gesture.
- [ManipulationEvents.DidHandOff](./didhandoff.md)
  The event that occurs during a manipulation gesture when someone passes an entity from one hand to the other.
- [ManipulationEvents.WillRelease](./willrelease.md)
  The event that occurs just as someone releases an entity during a manipulation gesture.
- [ManipulationEvents.WillEnd](./willend.md)
  The event that occurs at the end of a manipulation gesture, when the entity has reached its resting position, destination and the system no longer updates it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/didupdatetransform)*