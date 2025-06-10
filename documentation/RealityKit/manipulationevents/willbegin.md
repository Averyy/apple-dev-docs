# ManipulationEvents.WillBegin

**Framework**: RealityKit  
**Kind**: struct

A event triggered when an interaction is about to begin on a `ManipulationComponent`’s entity.

**Availability**:
- visionOS 26.0+ (Beta)

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
  An event triggered when an entity’s transform was updated during a `ManipulationComponent`.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  An event triggered when the object is directly handed off from one hand to another
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  A event triggered when an entity was released.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  An event triggered when the object has reached its destination and will no longer be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/willbegin)*