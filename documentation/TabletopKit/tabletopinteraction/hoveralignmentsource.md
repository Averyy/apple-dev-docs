# TabletopInteraction.HoverAlignmentSource

**Framework**: TabletopKit  
**Kind**: enum

An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum HoverAlignmentSource
```

## Topics

### Alignment sources
- [TabletopInteraction.HoverAlignmentSource.base](tabletopinteraction/hoveralignmentsource/base.md)
  The bottom face of the object (the face parallel the XZ plane with lowest value of Y)
- [TabletopInteraction.HoverAlignmentSource.baseOrTop](tabletopinteraction/hoveralignmentsource/baseortop.md)
  Either the top or bottom face (one of the two faces parallel to the XZ plane)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [TabletopInteraction.Constants](tabletopinteraction/constants.md)
- [TabletopInteraction.CollisionTargets](tabletopinteraction/collisiontargets.md)
  A set of targets for collision behaviors during an interaction
- [TabletopInteraction.DirectPickupBehavior](tabletopinteraction/directpickupbehavior.md)
  An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.
- [TabletopInteraction.DirectInteractionConstants](tabletopinteraction/directinteractionconstants.md)
  An object that represents the parameters of a direct interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.IndirectRotationAlignmentBehavior](tabletopinteraction/indirectrotationalignmentbehavior.md)
  An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.
- [TabletopInteraction.IndirectInteractionConstants](tabletopinteraction/indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](tabletopinteraction/hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentsource)*