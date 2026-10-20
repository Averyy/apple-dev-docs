# MIDIDeviceListGetNumberOfDevices(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Retrieves the number of devices in a device list.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceListGetNumberOfDevices(_ devList: MIDIDeviceListRef) -> Int
```

```c
extern ItemCount MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef devList);
```

#### Return Value

The number of devices in the list, or 0 if an error occurred.

## Parameters

- `devList`: The device list.

## See Also

### Managing Device Lists
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](./mididevicelistgetdevice%28_,_%29.md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](./mididevicelistadddevice%28_,_%29.md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](./mididevicelistdispose%28_%29.md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](./mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistgetnumberofdevices(_:))*