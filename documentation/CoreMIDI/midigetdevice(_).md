# MIDIGetDevice(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns a device from the system.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIGetDevice(_ deviceIndex0: Int) -> MIDIDeviceRef
```

```c
extern MIDIDeviceRef MIDIGetDevice(ItemCount deviceIndex0);
```

## Return Value

A reference to a device, or `NULL` if an error occurred.

## Discussion

Call this function to enumerate the devices in the system. To enumerate the entities in the system, walk through the devices and then walk through the device’s entities. When you iterate through the devices and entities in the system, you don’t visit virtual sources and destinations created by other clients.

A device iteration returns devices that are *offline* (they were present in the past but aren’t currently available), while iterations through the system’s sources and destinations don’t include the endpoints of offline devices. Instead, clients typically use [`MIDIGetNumberOfSources()`](./midigetnumberofsources%28%29.md), [`MIDIGetSource(_:)`](./midigetsource%28_%29.md), [`MIDIGetNumberOfDestinations()`](./midigetnumberofdestinations%28%29.md) and [`MIDIGetDestination(_:)`](./midigetdestination%28_%29.md).

## Parameters

- `deviceIndex0`: The index of the device to retrieve.

## See Also

### Device lookup
- [func MIDIGetNumberOfDevices() -> Int](./midigetnumberofdevices%28%29.md)
  Returns the number of devices in the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](./midigetnumberofexternaldevices%28%29.md)
  Returns the number of external MIDI devices in the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](./midigetexternaldevice%28_%29.md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](./mididevicegetnumberofentities%28_%29.md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](./mididevicegetentity%28_,_%29.md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](./midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetdevice(_:))*