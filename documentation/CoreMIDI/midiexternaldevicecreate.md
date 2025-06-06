# MIDIExternalDeviceCreate(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates an external MIDI device.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIExternalDeviceCreate(_ name: CFString, _ manufacturer: CFString, _ model: CFString, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Non-drivers may call this function to create external devices.

## Parameters

- `name`: The name of the device to create.
- `manufacturer`: The name of the device’s manufacturer.
- `model`: The model name of the device.
- `outDevice`: On successful return, this points to the newly created device.

## See Also

- [func MIDISetupAddExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupaddexternaldevice(_:).md)
  Adds an external MIDI device to the current MIDI setup.
- [func MIDISetupRemoveExternalDevice(MIDIDeviceRef) -> OSStatus](midisetupremoveexternaldevice(_:).md)
  Removes an external MIDI device from the current MIDI setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiexternaldevicecreate(_:_:_:_:))*