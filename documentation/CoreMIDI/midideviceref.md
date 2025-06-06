# MIDIDeviceRef

**Framework**: Core MIDI  
**Kind**: typealias

A MIDI device that contains entities.

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
typealias MIDIDeviceRef = MIDIObjectRef
```

#### Discussion

A device object derives from [`MIDIObjectRef`](midiobjectref.md). It doesn’t have an owning object.

## See Also

- [func MIDIDeviceCreate(MIDIDriverRef?, CFString, CFString, CFString, UnsafeMutablePointer<MIDIDeviceRef>) -> OSStatus](mididevicecreate(_:_:_:_:_:).md)
  Creates a new device object that corresponds to the available hardware.
- [func MIDIDeviceDispose(MIDIDeviceRef) -> OSStatus](mididevicedispose(_:).md)
  Disposes of a MIDI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midideviceref)*