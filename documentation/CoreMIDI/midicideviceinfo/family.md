# family

**Framework**: Core MIDI  
**Kind**: property

The family to which the device belongs.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var family: Data { get }
```

#### Discussion

This value is 2 bytes long.

## See Also

- [var manufacturerID: Data](midicideviceinfo/manufacturerid.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var modelNumber: Data](midicideviceinfo/modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](midicideviceinfo/revisionlevel.md)
  The revision number of the device model number.
- [var midiDestination: MIDIEndpointRef](midicideviceinfo/mididestination.md)
  The MIDI destination the device’s MIDI entity uses for capability inquiries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/family)*