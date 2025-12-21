# TabletopInteraction.IndirectRotationAlignmentBehavior.automatic

**Framework**: TabletopKit  
**Kind**: case

Automatically pick an alignment strategy based on the equipment size.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case automatic
```

## See Also

- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDevice](tabletopinteraction/indirectrotationalignmentbehavior/aligntoinputdevice.md)
  Align the equipment so its Z axis points towards the input devices and lays on the horizontal plane.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDeviceAndAutoFlip](tabletopinteraction/indirectrotationalignmentbehavior/aligntoinputdeviceandautoflip.md)
  Same as `alignToInputDevice` and also detect when the input device rotates enough to generate a flip of the equipment. When a flip is detected, the equipment will stay horizontal showing its back face.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.disabled](tabletopinteraction/indirectrotationalignmentbehavior/disabled.md)
  Use this value to disable the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectrotationalignmentbehavior/automatic)*