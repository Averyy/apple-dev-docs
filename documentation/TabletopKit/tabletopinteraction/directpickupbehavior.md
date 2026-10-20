# TabletopInteraction.DirectPickupBehavior

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DirectPickupBehavior
```

## Topics

### Creating a pickup behavior
- [init(deadZone: TabletopInteraction.DeadZone, collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior)](./directpickupbehavior/init%28deadzone,collisionresolution%29.md)
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](./directpickupbehavior/collisionresolutionbehavior.md)
  An object that represent the behavior that the object should have when colliding with the collision targets during the pickup phase.
### Getting the behavior properties
- [var collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](./directpickupbehavior/collisionresolution.md)
  The collision resolution allows to specify how the object should interaction with the collision targets during the pickup phase.
- [var deadZone: TabletopInteraction.DeadZone](./directpickupbehavior/deadzone.md)
  The dead zone allows to specify how much the input device should move from its initial pose to start moving the object.
- [static let `default`: TabletopInteraction.DirectPickupBehavior](./directpickupbehavior/default.md)
  The default behavior

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling collision behavior
- [TabletopInteraction.Constants](./constants.md)
- [TabletopInteraction.CollisionTargets](./collisiontargets.md)
  A set of targets for collision behaviors during an interaction
- [TabletopInteraction.DirectInteractionConstants](./directinteractionconstants.md)
  An object that represents the parameters of a direct interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.IndirectRotationAlignmentBehavior](./indirectrotationalignmentbehavior.md)
  An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.
- [TabletopInteraction.IndirectInteractionConstants](./indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](./hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](./hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](./programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/directpickupbehavior)*