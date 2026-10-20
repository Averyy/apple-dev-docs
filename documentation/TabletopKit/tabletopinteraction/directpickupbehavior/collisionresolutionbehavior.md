# TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

An object that represent the behavior that the object should have when colliding with the collision targets during the pickup phase.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum CollisionResolutionBehavior
```

## Topics

### Resolution behaviors
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior.automatic](./collisionresolutionbehavior/automatic.md)
  The automatic behavior moves and rotates the object to ensure that it does not penetrate the collision targets.
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior.disabled](./collisionresolutionbehavior/disabled.md)
  Use this value to disable collision resolution.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a pickup behavior
- [init(deadZone: TabletopInteraction.DeadZone, collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior)](./init%28deadzone,collisionresolution%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/directpickupbehavior/collisionresolutionbehavior)*