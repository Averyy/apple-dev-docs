# TabletopInteraction.DirectPickupBehavior

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DirectPickupBehavior
```

## Topics

### Creating a pickup behavior
- [init(deadZone: TabletopInteraction.DeadZone, collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior)](tabletopinteraction/directpickupbehavior/init(deadzone:collisionresolution:).md)
- [TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](tabletopinteraction/directpickupbehavior/collisionresolutionbehavior.md)
  An object that represent the behavior that the object should have when colliding with the collision targets during the pickup phase.
### Getting the behavior properties
- [var collisionResolution: TabletopInteraction.DirectPickupBehavior.CollisionResolutionBehavior](tabletopinteraction/directpickupbehavior/collisionresolution.md)
  The collision resolution allows to specify how the object should interaction with the collision targets during the pickup phase.
- [var deadZone: TabletopInteraction.DeadZone](tabletopinteraction/directpickupbehavior/deadzone.md)
  The dead zone allows to specify how much the input device should move from its initial pose to start moving the object.
- [static let `default`: TabletopInteraction.DirectPickupBehavior](tabletopinteraction/directpickupbehavior/default.md)
  The default behavior

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TabletopInteraction.Constants](tabletopinteraction/constants.md)
- [TabletopInteraction.CollisionTargets](tabletopinteraction/collisiontargets.md)
  A set of targets for collision behaviors during an interaction
- [TabletopInteraction.DirectInteractionConstants](tabletopinteraction/directinteractionconstants.md)
  An object that represents the parameters of a direct interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.IndirectRotationAlignmentBehavior](tabletopinteraction/indirectrotationalignmentbehavior.md)
  An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.
- [TabletopInteraction.IndirectInteractionConstants](tabletopinteraction/indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](tabletopinteraction/hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](tabletopinteraction/hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/directpickupbehavior)*