# TabletopInteraction.IndirectInteractionConstants

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct IndirectInteractionConstants
```

## Topics

### Creating an indirect interaction
- [init(rotationAlignment: TabletopInteraction.IndirectRotationAlignmentBehavior)](./indirectinteractionconstants/init%28rotationalignment%29.md)
### Getting the rotation alignment
- [var rotationAlignment: TabletopInteraction.IndirectRotationAlignmentBehavior](./indirectinteractionconstants/rotationalignment.md)
  The rotation alignment indicates how the equipment’s orientation should be automatically aligned during the course of the interaction.

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
- [TabletopInteraction.DirectPickupBehavior](./directpickupbehavior.md)
  An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.
- [TabletopInteraction.DirectInteractionConstants](./directinteractionconstants.md)
  An object that represents the parameters of a direct interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.IndirectRotationAlignmentBehavior](./indirectrotationalignmentbehavior.md)
  An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.
- [TabletopInteraction.HoverAlignmentBehavior](./hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](./hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](./programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectinteractionconstants)*