# MIDISetupAddExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

Adds an external MIDI device to the current MIDI setup.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDISetupAddExternalDevice(_ device: MIDIDeviceRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `device`: The device to add.

## See Also

- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](midiexternaldevicecreate(_:_:_:_:).md)
  Creates an external MIDI device.
- [func MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupremoveexternaldevice(_:).md)
  Removes an external MIDI device from the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupaddexternaldevice(_:))*