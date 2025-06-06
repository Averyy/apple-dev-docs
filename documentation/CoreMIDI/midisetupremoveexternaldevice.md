# MIDISetupRemoveExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

Removes an external MIDI device from the current MIDI setup.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDISetupRemoveExternalDevice(_ device: MIDIDeviceRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `device`: The device to remove.

## See Also

- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](midiexternaldevicecreate(_:_:_:_:).md)
  Creates an external MIDI device.
- [func MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupaddexternaldevice(_:).md)
  Adds an external MIDI device to the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupremoveexternaldevice(_:))*