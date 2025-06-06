# MIDIDeviceListGetDevice(_:_:)

**Framework**: Core MIDI  
**Kind**: func

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

#### Return Value

A reference to a device, or `NULL` if an error occurred.

## Parameters

- `devList`: The device list.
- `index0`: The index of the device to return.

## See Also

- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](mididevicelistgetnumberofdevices(_:).md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](mididevicelistadddevice(_:_:).md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](mididevicelistdispose(_:).md)
  Disposes of a device list, but not its devices.
- [typealias MIDIDeviceListRef](mididevicelistref.md)
  A list of MIDI devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistgetdevice(_:_:))*