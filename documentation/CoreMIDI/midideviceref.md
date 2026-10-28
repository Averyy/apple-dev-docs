# MIDIDeviceRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A MIDI device that contains entities.

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
typealias MIDIDeviceRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIDeviceRef;
```

## Discussion

A device object derives from [`MIDIObjectRef`](./midiobjectref.md). It doesn’t have an owning object.

## See Also

### Managing Device Lifecyle
- [func MIDIDeviceCreate(MIDIDriverRef?, CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](./mididevicecreate%28_,_,_,_,_%29.md)
  Creates a new device object that corresponds to the available hardware.
- [func MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus](./mididevicedispose%28_%29.md)
  Disposes of a MIDI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midideviceref)*