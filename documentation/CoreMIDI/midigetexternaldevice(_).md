# MIDIGetExternalDevice(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern MIDIDeviceRef MIDIGetExternalDevice(ItemCount deviceIndex0);
```

## Return Value

A reference to a device, or `NULL` if an error occurred.

## Discussion

Call this function to enumerate the external devices in the system.

## Parameters

- `deviceIndex0`: The index of the device to return.

## See Also

### Device lookup
- [func MIDIGetNumberOfDevices() -> Int](./midigetnumberofdevices%28%29.md)
  Returns the number of devices in the system.
- [func MIDIGetDevice(Int) -> MIDIDeviceRef](./midigetdevice%28_%29.md)
  Returns a device from the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](./midigetnumberofexternaldevices%28%29.md)
  Returns the number of external MIDI devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](./mididevicegetnumberofentities%28_%29.md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](./mididevicegetentity%28_,_%29.md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](./midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetexternaldevice(_:))*