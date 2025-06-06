# MIDIDeviceListDispose(_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

An `OSStatus` result code.

## Parameters

- `devList`: The device list of which you dispose.

## See Also

- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](mididevicelistgetnumberofdevices(_:).md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](mididevicelistgetdevice(_:_:).md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](mididevicelistadddevice(_:_:).md)
  Adds the specified device to the device list.
- [typealias MIDIDeviceListRef](mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistdispose(_:))*