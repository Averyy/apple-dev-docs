# MIDIDeviceListDispose(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Disposes of a device list, but not its devices.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.1+
- visionOS 1.0+

## Declaration

```swift
func MIDIDeviceListDispose(_ devList: MIDIDeviceListRef) -> OSStatus
```

```c
extern OSStatus MIDIDeviceListDispose(MIDIDeviceListRef devList);
```

## Return Value

An `OSStatus` result code.

## Parameters

- `devList`: The device list of which you dispose.

## See Also

### Managing Device Lists
- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](./mididevicelistgetnumberofdevices%28_%29.md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](./mididevicelistgetdevice%28_,_%29.md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](./mididevicelistadddevice%28_,_%29.md)
  Adds the specified device to the device list.
- [typealias MIDIDeviceListRef](./mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistdispose(_:))*