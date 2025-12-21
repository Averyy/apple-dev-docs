# ExtendedControlEvent

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct ExtendedControlEvent
```

## Topics

### Initializers
- [init()](extendedcontrolevent/init.md)
- [init(groupID: MusicDeviceGroupID, controlID: AudioUnitParameterID, value: AudioUnitParameterValue)](extendedcontrolevent/init(groupid:controlid:value:).md)
### Instance Properties
- [var controlID: AudioUnitParameterID](extendedcontrolevent/controlid.md)
- [var groupID: MusicDeviceGroupID](extendedcontrolevent/groupid.md)
- [var value: AudioUnitParameterValue](extendedcontrolevent/value.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MIDIEndpointRef](../CoreMIDI/MIDIEndpointRef.md)
  A MIDI source or destination an entity owns.
- [typealias MagicCookieInfo](magiccookieinfo.md)
  A structure holding magic cookie information.
- [typealias NoteInstanceID](noteinstanceid.md)
- [typealias ReadBytesFDF](readbytesfdf.md)
- [typealias ReadPacketDataFDF](readpacketdatafdf.md)
- [typealias ReadPacketsFDF](readpacketsfdf.md)
- [typealias SetPropertyFDF](setpropertyfdf.md)
- [typealias SetUserDataFDF](setuserdatafdf.md)
- [typealias WriteBytesFDF](writebytesfdf.md)
- [typealias WritePacketsFDF](writepacketsfdf.md)
- [typealias AudioSessionPropertyID](audiosessionpropertyid.md)
  The data type for an audio session property identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extendedcontrolevent)*