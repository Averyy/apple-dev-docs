# MIDIGetNumberOfExternalDevices()

**Framework**: Core MIDI  
**Kind**: func

Returns the number of external MIDI devices in the system.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIGetNumberOfExternalDevices() -> Int
```

#### Return Value

The number of external devices in the system, or 0 if an error occurred.

#### Discussion

External MIDI devices connect to driver endpoints using a standard MIDI cable. Their presence is optional only when a UI (such as Audio MIDI Setup) adds them.

## See Also

- [func MIDIGetNumberOfDevices() -> Int](midigetnumberofdevices().md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](midigetdevice(_:).md)
  Returns a device from the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](midigetexternaldevice(_:).md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](mididevicegetnumberofentities(_:).md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](mididevicegetentity(_:_:).md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetnumberofexternaldevices())*