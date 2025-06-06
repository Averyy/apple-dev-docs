# MIDIDeviceListRef

**Framework**: Core MIDI  
**Kind**: typealias

A list of MIDI devices.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias MIDIDeviceListRef = MIDIObjectRef
```

#### Discussion

This object doesn’t own the devices, so disposing it doesn’t dispose the devices it references.

## See Also

- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](mididevicelistgetnumberofdevices(_:).md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](mididevicelistgetdevice(_:_:).md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](mididevicelistadddevice(_:_:).md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](mididevicelistdispose(_:).md)
  Disposes of a device list, but not its devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistref)*