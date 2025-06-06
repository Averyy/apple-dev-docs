# midiDestination

**Framework**: Core MIDI  
**Kind**: property

The MIDI destination with which the session is communicating.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var midiDestination: MIDIEntityRef { get }
```

## See Also

- [var deviceInfo: MIDICIDeviceInfo](midicisession/deviceinfo.md)
  Information about a MIDI-CI device.
- [var maxSysExSize: NSNumber](midicisession/maxsysexsize.md)
  The maximum size of System Exclusive (SysEx) messages.
- [var maxPropertyRequests: NSNumber](midicisession/maxpropertyrequests.md)
  The maximum number of simultaneous property exchange requests, if supported.
- [var supportsProfileCapability: Bool](midicisession/supportsprofilecapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI profile’s capability.
- [var supportsPropertyCapability: Bool](midicisession/supportspropertycapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI property exchange capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/mididestination)*