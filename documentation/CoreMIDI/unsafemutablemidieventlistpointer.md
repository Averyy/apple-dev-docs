# UnsafeMutableMIDIEventListPointer

**Framework**: Core MIDI  
**Kind**: struct

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
struct UnsafeMutableMIDIEventListPointer
```

## Topics

### Initializers
- [init?(UnsafeMutablePointer<MIDIEventList>?, wordSize: Int)](unsafemutablemidieventlistpointer/init(_:wordsize:).md)
- [init(UnsafeMutablePointer<MIDIEventList>, wordSize: Int, inProtocol: MIDIProtocolID)](unsafemutablemidieventlistpointer/init(_:wordsize:inprotocol:).md)
### Instance Properties
- [var count: Int](unsafemutablemidieventlistpointer/count.md)
- [var lastPacket: UnsafeMutablePointer<MIDIEventPacket>?](unsafemutablemidieventlistpointer/lastpacket.md)
- [var listSizeInBytes: Int](unsafemutablemidieventlistpointer/listsizeinbytes.md)
- [var midiProtocol: MIDIProtocolID](unsafemutablemidieventlistpointer/midiprotocol.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, words: [UInt32]) -> UnsafePointer<MIDIEventPacket>?](unsafemutablemidieventlistpointer/append(timestamp:words:).md)
- [func clear()](unsafemutablemidieventlistpointer/clear.md)

## Relationships

### Conforms To
- [Sequence](../Swift/Sequence.md)

## See Also

- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistinit(_:_:).md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistadd(_:_:_:_:_:_:).md)
  Adds an event to an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventpacketnext(_:).md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
- [func MIDISendEventList(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midisendeventlist(_:_:_:).md)
  Sends MIDI events to a destination.
- [func MIDIReceivedEventList(MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midireceivedeventlist(_:_:).md)
  Distributes incoming MIDI events from a source to its connected client input ports.
- [struct MIDIEventList](midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidieventlistpointer)*