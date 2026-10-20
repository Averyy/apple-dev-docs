# TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDevice

**Framework**: TabletopKit  
**Kind**: case  
**Role**: Case

Align the equipment so its Z axis points towards the input devices and lays on the horizontal plane.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case alignToInputDevice
```

## See Also

### Alignment behaviors
- [TabletopInteraction.IndirectRotationAlignmentBehavior.alignToInputDeviceAndAutoFlip](./aligntoinputdeviceandautoflip.md)
  Same as `alignToInputDevice` and also detect when the input device rotates enough to generate a flip of the equipment. When a flip is detected, the equipment will stay horizontal showing its back face.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.automatic](./automatic.md)
  Automatically pick an alignment strategy based on the equipment size.
- [TabletopInteraction.IndirectRotationAlignmentBehavior.disabled](./disabled.md)
  Use this value to disable the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/indirectrotationalignmentbehavior/aligntoinputdevice)*