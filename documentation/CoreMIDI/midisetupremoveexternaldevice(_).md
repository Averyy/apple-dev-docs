# MIDISetupRemoveExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDISetupRemoveExternalDevice(MIDIDeviceRef device);
```

## Return Value

An `OSStatus` result code.

## Parameters

- `device`: The device to remove.

## See Also

### Managing External Devices
- [func MIDIExternalDeviceCreate(CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](./midiexternaldevicecreate%28_,_,_,_%29.md)
  Creates an external MIDI device.
- [func MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus](./midisetupaddexternaldevice%28_%29.md)
  Adds an external MIDI device to the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupremoveexternaldevice(_:))*