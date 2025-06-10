# TabletopInteraction.IndirectRotationAlignmentBehavior

**Framework**: TabletopKit  
**Kind**: enum

An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum IndirectRotationAlignmentBehavior
```

## Topics

### Enumeration Cases
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectrotationalignmentbehavior)*