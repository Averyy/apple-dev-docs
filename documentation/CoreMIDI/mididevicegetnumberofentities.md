# MIDIDeviceGetNumberOfEntities(_:)

**Framework**: Core MIDI  
**Kind**: func

Returns the number of entities in a device.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceGetNumberOfEntities(_ device: MIDIDeviceRef) -> Int
```

#### Return Value

The number of entities the device contains, or 0 if an error occurred.

## Parameters

- `device`: The device to query.

## See Also

- [func MIDIGetNumberOfDevices() -> Int](midigetnumberofdevices().md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](midigetdevice(_:).md)
  Returns a device from the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](midigetnumberofexternaldevices().md)
  Returns the number of external MIDI devices in the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](midigetexternaldevice(_:).md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](mididevicegetentity(_:_:).md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicegetnumberofentities(_:))*