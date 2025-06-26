# ManipulationEvents.WillEnd

**Framework**: RealityKit  
**Kind**: struct

The event that occurs at the end of a manipulation gesture, when the entity has reached its resting position, destination and the system no longer updates it.

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
  The event that occurs when someone is about to start an entity manipulation gesture.
- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
  The event that occurs repeatedly when the entity’s transform updates during a manipulation gesture.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  The event that occurs during a manipulation gesture when someone passes an entity from one hand to the other.
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  The event that occurs just as someone releases an entity during a manipulation gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents/willend)*