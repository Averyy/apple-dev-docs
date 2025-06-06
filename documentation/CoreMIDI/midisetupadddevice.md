# MIDISetupAddDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

Adds a driver-owned MIDI device to the current MIDI setup.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDISetupAddDevice(_ device: MIDIDeviceRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Only MIDI drivers may call this function.

## Parameters

- `device`: The device to add.

## See Also

- [func MIDISetupRemoveDevice(MIDIDeviceRef) -> OSStatus](midisetupremovedevice(_:).md)
  Removes a driver-owned MIDI device from the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupadddevice(_:))*