# maxPropertyRequests

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The maximum number of simultaneous property exchange requests, if supported.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var maxPropertyRequests: NSNumber { get }
```

```objc
@property (nonatomic, readonly) NSNumber * maxPropertyRequests;
```

## See Also

### Inspecting a Session
- [var deviceInfo: MIDICIDeviceInfo](./deviceinfo.md)
  Information about a MIDI-CI device.
- [var maxSysExSize: NSNumber](./maxsysexsize.md)
  The maximum size of System Exclusive (SysEx) messages.
- [var midiDestination: MIDIEntityRef](./mididestination.md)
  The MIDI destination with which the session is communicating.
- [var supportsProfileCapability: Bool](./supportsprofilecapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI profile’s capability.
- [var supportsPropertyCapability: Bool](./supportspropertycapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI property exchange capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/maxpropertyrequests)*