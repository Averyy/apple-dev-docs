# MIDIDeviceListGetDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Retrieves a MIDI device from a device list.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceListGetDevice(_ devList: MIDIDeviceListRef, _ index0: Int) -> MIDIDeviceRef
```

```c
extern MIDIDeviceRef MIDIDeviceListGetDevice(MIDIDeviceListRef devList, ItemCount index0);
```

#### Return Value

A reference to a device, or `NULL` if an error occurred.

## Parameters

- `devList`: The device list.
- `index0`: The index of the device to return.

## See Also

### Managing Device Lists
- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](./mididevicelistgetnumberofdevices%28_%29.md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](./mididevicelistadddevice%28_,_%29.md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](./mididevicelistdispose%28_%29.md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](./mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistgetdevice(_:_:))*