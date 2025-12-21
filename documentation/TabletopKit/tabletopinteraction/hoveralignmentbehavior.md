# TabletopInteraction.HoverAlignmentBehavior

**Framework**: TabletopKit  
**Kind**: enum

An object that describes how the controlled equipment should behave when approaching a target.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum HoverAlignmentBehavior
```

## Topics

### Alignment Behaviors
- [case align(TabletopInteraction.HoverAlignmentSource, with: TabletopInteraction.CollisionTargets)](tabletopinteraction/hoveralignmentbehavior/align(_:with:).md)
  `align` indicates that the equipment should orient itself to align the closest `source` to the target. The equipment’s movement is also limited to prevent it from penetrating the target.
- [TabletopInteraction.HoverAlignmentBehavior.automatic(targets:)](tabletopinteraction/hoveralignmentbehavior/automatic(targets:).md)
  `automatic` picks a strategy based on the equipment size.
- [TabletopInteraction.HoverAlignmentBehavior.disabled](tabletopinteraction/hoveralignmentbehavior/disabled.md)
  Use this value to disable the behavior.
- [TabletopInteraction.HoverAlignmentBehavior.stop(at:)](tabletopinteraction/hoveralignmentbehavior/stop(at:).md)
  `stop` indicates that the equipment movement should stop when pushed into the target, to avoid penetration. The orientation of the equipment is not affected.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
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
- [TabletopInteraction.HoverAlignmentSource](tabletopinteraction/hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/hoveralignmentbehavior)*