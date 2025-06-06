# MIDISetupRemoveDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

Removes a driver-owned MIDI device from the current MIDI setup.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDISetupRemoveDevice(_ device: MIDIDeviceRef) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Typically, only a studio-configuration editor calls this function to remove a device that’s offline and which the user has specified as permanently missing. It’s a good practice to have drivers set the deviceʼs [`kMIDIPropertyOffline`](kmidipropertyoffline.md) to 1, instead of removing the device from the setup, so if the device reappears later, the system preserves the deviceʼs property state.

## Parameters

- `device`: The device to remove.

## See Also

- [func MIDISetupAddDevice(MIDIDeviceRef) -> OSStatus](midisetupadddevice(_:).md)
  Adds a driver-owned MIDI device to the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisetupremovedevice(_:))*