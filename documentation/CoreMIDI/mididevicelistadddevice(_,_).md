# MIDIDeviceListAddDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Adds the specified device to the device list.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceListAddDevice(_ devList: MIDIDeviceListRef, _ dev: MIDIDeviceRef) -> OSStatus
```

```c
extern OSStatus MIDIDeviceListAddDevice(MIDIDeviceListRef devList, MIDIDeviceRef dev);
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `devList`: The device list.
- `dev`: The device to add to the list.

## See Also

### Managing Device Lists
- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](./mididevicelistgetnumberofdevices%28_%29.md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](./mididevicelistgetdevice%28_,_%29.md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](./mididevicelistdispose%28_%29.md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](./mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistadddevice(_:_:))*