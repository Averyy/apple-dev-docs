# MIDIGetDevice(_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

A reference to a device, or `NULL` if an error occurred.

#### Discussion

Call this function to enumerate the devices in the system. To enumerate the entities in the system, walk through the devices and then walk through the device’s entities. When you iterate through the devices and entities in the system, you don’t visit virtual sources and destinations created by other clients.

A device iteration returns devices that are  (they were present in the past but aren’t currently available), while iterations through the system’s sources and destinations don’t include the endpoints of offline devices. Instead, clients typically use [`MIDIGetNumberOfSources()`](midigetnumberofsources().md), [`MIDIGetSource(_:)`](midigetsource(_:).md), [`MIDIGetNumberOfDestinations()`](midigetnumberofdestinations().md) and [`MIDIGetDestination(_:)`](midigetdestination(_:).md).

## Parameters

- `deviceIndex0`: The index of the device to retrieve.

## See Also

- [func MIDIGetNumberOfDevices() -> Int](midigetnumberofdevices().md)
  Returns the number of devices in the system.
- [func MIDIGetNumberOfExternalDevices() -> Int](midigetnumberofexternaldevices().md)
  Returns the number of external MIDI devices in the system.
- [func MIDIGetExternalDevice(Int) -> MIDIDeviceRef](midigetexternaldevice(_:).md)
  Returns one of the external devices in the system.
- [func MIDIDeviceGetNumberOfEntities(MIDIDeviceRef) -> Int](mididevicegetnumberofentities(_:).md)
  Returns the number of entities in a device.
- [func MIDIDeviceGetEntity(MIDIDeviceRef, Int) -> MIDIEntityRef](mididevicegetentity(_:_:).md)
  Returns the device’s entity at a specific index.
- [typealias MIDIDeviceRef](midideviceref.md)
  A MIDI device that contains entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midigetdevice(_:))*