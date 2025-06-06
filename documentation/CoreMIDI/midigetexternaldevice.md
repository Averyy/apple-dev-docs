# MIDIGetExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

Returns one of the external devices in the system.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIGetExternalDevice(_ deviceIndex0: Int) -> MIDIDeviceRef
```

#### Return Value

A reference to a device, or `NULL` if an error occurred.

#### Discussion

Call this function to enumerate the external devices in the system.

## Parameters

- `deviceIndex0`: The index of the device to return.

## See Also

- [func MIDIGetNumberOfDevices() -> Int](midigetnumberofdevices().md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](midigetdevice(_:).md)
  Returns a device from the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](midigetnumberofexternaldevices().md)
  Returns the number of external MIDI devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](mididevicegetnumberofentities(_:).md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](mididevicegetentity(_:_:).md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetexternaldevice(_:))*