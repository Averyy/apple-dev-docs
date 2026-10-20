# MIDISetupAddExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDISetupAddExternalDevice(MIDIDeviceRef device);
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `device`: The device to add.

## See Also

### Managing External Devices
- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](./midiexternaldevicecreate%28_,_,_,_%29.md)
  Creates an external MIDI device.
- [func MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus](./midisetupremoveexternaldevice%28_%29.md)
  Removes an external MIDI device from the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupaddexternaldevice(_:))*