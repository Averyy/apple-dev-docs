# SetPropertyFDF

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias SetPropertyFDF = (UnsafeMutableRawPointer, AudioFilePropertyID, UInt32, UnsafeRawPointer) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, const void *) SetPropertyFDF;
```

## See Also

### Data Types
- [struct ExtendedControlEvent](./extendedcontrolevent.md)
- [typealias MIDIEndpointRef](../CoreMIDI/midiendpointref.md)
  A MIDI source or destination an entity owns.
- [typealias MagicCookieInfo](./magiccookieinfo.md)
  A structure holding magic cookie information.
- [typealias NoteInstanceID](./noteinstanceid.md)
- [typealias ReadBytesFDF](./readbytesfdf.md)
- [typealias ReadPacketDataFDF](./readpacketdatafdf.md)
- [typealias ReadPacketsFDF](./readpacketsfdf.md)
- [typealias SetUserDataFDF](./setuserdatafdf.md)
- [typealias WriteBytesFDF](./writebytesfdf.md)
- [typealias WritePacketsFDF](./writepacketsfdf.md)
- [typealias AudioSessionPropertyID](./audiosessionpropertyid.md)
  The data type for an audio session property identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/setpropertyfdf)*