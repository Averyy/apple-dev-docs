# family

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The family to which the device belongs.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var family: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * family;
```

## Discussion

This value is 2 bytes long.

## See Also

### Inspecting a Device
- [var manufacturerID: Data](./manufacturerid.md)
  The MIDI System Exclusive (SysEx) ID of the device manufacturer.
- [var modelNumber: Data](./modelnumber.md)
  The model number of the device.
- [var revisionLevel: Data](./revisionlevel.md)
  The revision number of the device model number.
- [var midiDestination: MIDIEndpointRef](./mididestination.md)
  The MIDI destination the device’s MIDI entity uses for capability inquiries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicideviceinfo/family)*