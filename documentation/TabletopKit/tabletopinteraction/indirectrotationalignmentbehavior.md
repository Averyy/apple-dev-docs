# TabletopInteraction.IndirectRotationAlignmentBehavior

**Framework**: TabletopKit  
**Kind**: enum

An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum IndirectRotationAlignmentBehavior
```

## Topics

### Alignment behaviors
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDevice](tabletopinteraction/indirectrotationalignmentbehavior/aligntoinputdevice.md)
  Align the equipment so its Z axis points towards the input devices and lays on the horizontal plane.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDeviceAndAutoFlip](tabletopinteraction/indirectrotationalignmentbehavior/aligntoinputdeviceandautoflip.md)
  Same as `alignToInputDevice` and also detect when the input device rotates enough to generate a flip of the equipment. When a flip is detected, the equipment will stay horizontal showing its back face.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.automatic](tabletopinteraction/indirectrotationalignmentbehavior/automatic.md)
  Automatically pick an alignment strategy based on the equipment size.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.disabled](tabletopinteraction/indirectrotationalignmentbehavior/disabled.md)
  Use this value to disable the behavior.

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
- [TabletopInteraction.IndirectInteractionConstants](tabletopinteraction/indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](tabletopinteraction/hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](tabletopinteraction/hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectrotationalignmentbehavior)*