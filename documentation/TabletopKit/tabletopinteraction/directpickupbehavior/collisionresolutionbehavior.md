# TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior

**Framework**: TabletopKit  
**Kind**: enum

An object that represent the behavior that the object should have when colliding with the collision targets during the pickup phase.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum CollisionResolutionBehavior
```

## Topics

### Resolution behaviors
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior.automatic](tabletopinteraction/directpickupbehavior/collisionresolutionbehavior/automatic.md)
  The automatic behavior moves and rotates the object to ensure that it does not penetrate the collision targets.
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior.disabled](tabletopinteraction/directpickupbehavior/collisionresolutionbehavior/disabled.md)
  Use this value to disable collision resolution.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(deadZone: TabletopInteraction.DeadZone, collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior)](tabletopinteraction/directpickupbehavior/init(deadzone:collisionresolution:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/directpickupbehavior/collisionresolutionbehavior)*