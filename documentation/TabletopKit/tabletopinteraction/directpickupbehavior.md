# TabletopInteraction.DirectPickupBehavior

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DirectPickupBehavior
```

## Topics

### Initializers
- [init(deadZone: TabletopInteraction.DeadZone, collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior)](tabletopinteraction/directpickupbehavior/init(deadzone:collisionresolution:).md)
### Instance Properties
- [var collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](tabletopinteraction/directpickupbehavior/collisionresolution.md)
  The collision resolution allows to specify how the object should interaction with the collision targets during the pickup phase.
- [var deadZone: TabletopInteraction.DeadZone](tabletopinteraction/directpickupbehavior/deadzone.md)
  The dead zone allows to specify how much the input device should move from its initial pose to start moving the object.
### Type Properties
- [static let `default`: TabletopInteraction.DirectPickupBehavior](tabletopinteraction/directpickupbehavior/default.md)
  The default behavior
### Enumerations
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](tabletopinteraction/directpickupbehavior/collisionresolutionbehavior.md)
  An object that represent the behavior that the object should have when colliding with the collision targets during the pickup phase.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/directpickupbehavior)*