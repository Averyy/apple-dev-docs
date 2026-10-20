# ExtendedControlEvent

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct ExtendedControlEvent
```

```c
typedef struct ExtendedControlEvent { ... } ExtendedControlEvent;
```

## Topics

### Initializers
- [init()](./extendedcontrolevent/init%28%29.md)
- [init(groupID: MusicDeviceGroupID, controlID: AudioUnitParameterID, value: AudioUnitParameterValue)](./extendedcontrolevent/init%28groupid,controlid,value%29.md)
### Instance Properties
- [var controlID: AudioUnitParameterID](./extendedcontrolevent/controlid.md)
- [var groupID: MusicDeviceGroupID](./extendedcontrolevent/groupid.md)
- [var value: AudioUnitParameterValue](./extendedcontrolevent/value.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [typealias MIDIEndpointRef](../CoreMIDI/midiendpointref.md)
  A MIDI source or destination an entity owns.
- [typealias MagicCookieInfo](./magiccookieinfo.md)
  A structure holding magic cookie information.
- [typealias NoteInstanceID](./noteinstanceid.md)
- [typealias ReadBytesFDF](./readbytesfdf.md)
- [typealias ReadPacketDataFDF](./readpacketdatafdf.md)
- [typealias ReadPacketsFDF](./readpacketsfdf.md)
- [typealias SetPropertyFDF](./setpropertyfdf.md)
- [typealias SetUserDataFDF](./setuserdatafdf.md)
- [typealias WriteBytesFDF](./writebytesfdf.md)
- [typealias WritePacketsFDF](./writepacketsfdf.md)
- [typealias AudioSessionPropertyID](./audiosessionpropertyid.md)
  The data type for an audio session property identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extendedcontrolevent)*