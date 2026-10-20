# TabletopInteraction.IndirectRotationAlignmentBehavior

**Framework**: TabletopKit  
**Kind**: enum  
**Role**: Enumeration

An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum IndirectRotationAlignmentBehavior
```

## Topics

### Alignment behaviors
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDevice](./indirectrotationalignmentbehavior/aligntoinputdevice.md)
  Align the equipment so its Z axis points towards the input devices and lays on the horizontal plane.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDeviceAndAutoFlip](./indirectrotationalignmentbehavior/aligntoinputdeviceandautoflip.md)
  Same as `alignToInputDevice` and also detect when the input device rotates enough to generate a flip of the equipment. When a flip is detected, the equipment will stay horizontal showing its back face.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.automatic](./indirectrotationalignmentbehavior/automatic.md)
  Automatically pick an alignment strategy based on the equipment size.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.disabled](./indirectrotationalignmentbehavior/disabled.md)
  Use this value to disable the behavior.

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
- [TabletopInteraction.IndirectInteractionConstants](./indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](./hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](./hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](./programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectrotationalignmentbehavior)*