# MIDIDeviceGetEntity(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns the device’s entity at a specific index.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceGetEntity(_ device: MIDIDeviceRef, _ entityIndex0: Int) -> MIDIEntityRef
```

```c
extern MIDIEntityRef MIDIDeviceGetEntity(MIDIDeviceRef device, ItemCount entityIndex0);
```

#### Return Value

An entity reference, or `NULL` if an error occurred.

## Parameters

- `device`: The device to query.
- `entityIndex0`: The entity index.

## See Also

### Device lookup
- [func MIDIGetNumberOfDevices() -> Int](./midigetnumberofdevices%28%29.md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](./midigetdevice%28_%29.md)
  Returns a device from the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](./midigetnumberofexternaldevices%28%29.md)
  Returns the number of external MIDI devices in the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](./midigetexternaldevice%28_%29.md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](./mididevicegetnumberofentities%28_%29.md)
  Returns the number of entities in a device.
- [typealias MIDIDeviceRef](./midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicegetentity(_:_:))*