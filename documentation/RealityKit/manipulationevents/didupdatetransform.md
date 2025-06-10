# ManipulationEvents.DidUpdateTransform

**Framework**: RealityKit  
**Kind**: struct

An event triggered when an entity’s transform was updated during a `ManipulationComponent`.

**Availability**:
- visionOS 26.0+ (Beta)

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
  A event triggered when an interaction is about to begin on a `ManipulationComponent`’s entity.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  An event triggered when the object is directly handed off from one hand to another
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  A event triggered when an entity was released.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  An event triggered when the object has reached its destination and will no longer be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/didupdatetransform)*