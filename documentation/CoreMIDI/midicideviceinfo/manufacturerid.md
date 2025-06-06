# manufacturerID

**Framework**: Core MIDI  
**Kind**: property

The MIDI System Exclusive (SysEx) ID of the device manufacturer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var manufacturerID: Data { get }
```

#### Discussion

This value is 3 bytes long.

The framework pads single-byte System Exclusive (SysEx) IDs with trailing zeros. For example, Apple’s SysEx ID, 0x11, is `0x110000`.

## See Also

- [var family: Data](midicideviceinfo/family.md)
  The family to which the device belongs.
- [var modelNumber: Data](midicideviceinfo/modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](midicideviceinfo/revisionlevel.md)
  The revision number of the device model number.
- [var midiDestination: MIDIEndpointRef](midicideviceinfo/mididestination.md)
  The MIDI destination the device’s MIDI entity uses for capability inquiries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/manufacturerid)*