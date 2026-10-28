# MIDIDeviceListRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A list of MIDI devices.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias MIDIDeviceListRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIDeviceListRef;
```

## Discussion

This object doesn’t own the devices, so disposing it doesn’t dispose the devices it references.

## See Also

### Managing Device Lists
- [func MIDIDeviceListGetNumberOfDevices(MIDIDeviceListRef) -> Int](./mididevicelistgetnumberofdevices%28_%29.md)
  Retrieves the number of devices in a device list.
- [func MIDIDeviceListGetDevice(MIDIDeviceListRef, Int) -> MIDIDeviceRef](./mididevicelistgetdevice%28_,_%29.md)
  Retrieves a MIDI device from a device list.
- [func MIDIDeviceListAddDevice(MIDIDeviceListRef, MIDIDeviceRef) -> OSStatus](./mididevicelistadddevice%28_,_%29.md)
  Adds the specified device to the device list.
- [func MIDIDeviceListDispose(MIDIDeviceListRef) -> OSStatus](./mididevicelistdispose%28_%29.md)
  Disposes of a device list, but not its devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididevicelistref)*