# TabletopInteraction.HoverAlignmentSource

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum HoverAlignmentSource
```

## Topics

### Alignment sources
- [TabletopInteraction.HoverAlignmentSource.base](./hoveralignmentsource/base.md)
  The bottom face of the object (the face parallel the XZ plane with lowest value of Y)
- [TabletopInteraction.HoverAlignmentSource.baseOrTop](./hoveralignmentsource/baseortop.md)
  Either the top or bottom face (one of the two faces parallel to the XZ plane)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
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
- [TabletopInteraction.IndirectInteractionConstants](./indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](./hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.ProgrammaticInteractionConstants](./programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentsource)*