# TabletopInteraction.Constants

**Framework**: TabletopKit  
**Kind**: enum

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum Constants
```

## Topics

### Table interactions
- [case direct(TabletopInteraction.DirectInteractionConstants)](tabletopinteraction/constants/direct(_:).md)
- [case indirect(TabletopInteraction.IndirectInteractionConstants)](tabletopinteraction/constants/indirect(_:).md)
- [case programmatic(TabletopInteraction.ProgrammaticInteractionConstants)](tabletopinteraction/constants/programmatic(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [TabletopInteraction.HoverAlignmentSource](tabletopinteraction/hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/constants)*