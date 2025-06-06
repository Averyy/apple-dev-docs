# MIDIDeviceListAddDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

An `OSStatus` result code.

## Parameters

- `devList`: The device list.
- `dev`: The device to add to the list.

## See Also

- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](mididevicelistgetnumberofdevices(_:).md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](mididevicelistgetdevice(_:_:).md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](mididevicelistdispose(_:).md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistadddevice(_:_:))*