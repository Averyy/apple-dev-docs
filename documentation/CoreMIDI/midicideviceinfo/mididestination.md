# midiDestination

**Framework**: Core MIDI  
**Kind**: property

The MIDI destination the device’s MIDI entity uses for capability inquiries.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var midiDestination: MIDIEndpointRef { get }
```

## See Also

- [var manufacturerID: Data](midicideviceinfo/manufacturerid.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var family: Data](midicideviceinfo/family.md)
  The family to which the device belongs.
- [var modelNumber: Data](midicideviceinfo/modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](midicideviceinfo/revisionlevel.md)
  The revision number of the device model number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/mididestination)*