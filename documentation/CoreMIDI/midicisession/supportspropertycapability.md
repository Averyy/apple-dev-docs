# supportsPropertyCapability

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the entity supports the MIDI-CI property exchange capability.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var supportsPropertyCapability: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsPropertyCapability;
```

## See Also

### Inspecting a Session
- [var deviceInfo: MIDICIDeviceInfo](./deviceinfo.md)
  Information about a MIDI-CI device.
- [var maxSysExSize: NSNumber](./maxsysexsize.md)
  The maximum size of System Exclusive (SysEx) messages.
- [var midiDestination: MIDIEntityRef](./mididestination.md)
  The MIDI destination with which the session is communicating.
- [var maxPropertyRequests: NSNumber](./maxpropertyrequests.md)
  The maximum number of simultaneous property exchange requests, if supported.
- [var supportsProfileCapability: Bool](./supportsprofilecapability.md)
  A Boolean value that indicates whether the entity supports the MIDI-CI profile’s capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicisession/supportspropertycapability)*