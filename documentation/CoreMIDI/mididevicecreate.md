# MIDIDeviceCreate(_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates a new device object that corresponds to the available hardware.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceCreate(_ owner: MIDIDriverRef?, _ name: CFString, _ manufacturer: CFString, _ model: CFString, _ outDevice: UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Nondrivers may call this function to create external devices.

## Parameters

- `owner`: The driver that creates the device, or   for a non-driver.
- `name`: The name of the new device.
- `manufacturer`: The name of the device’s manufacturer.
- `model`: The name of the model of the device.
- `outDevice`: On successful return, points to the newly created device.

## See Also

- [func MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus](mididevicedispose(_:).md)
  Disposes of a MIDI device.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicecreate(_:_:_:_:_:))*