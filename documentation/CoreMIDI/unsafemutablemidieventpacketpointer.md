# UnsafeMutableMIDIEventPacketPointer

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
struct UnsafeMutableMIDIEventPacketPointer
```

## Topics

### Initializers
- [init(UnsafeMutablePointer<MIDIEventPacket>)](unsafemutablemidieventpacketpointer/init(_:)-2pp97.md)
- [init?(UnsafeMutablePointer<MIDIEventPacket>?)](unsafemutablemidieventpacketpointer/init(_:)-91lug.md)
### Instance Properties
- [var count: Int](unsafemutablemidieventpacketpointer/count.md)
- [var timeStamp: Int](unsafemutablemidieventpacketpointer/timestamp.md)
### Default Implementations
- [MutableCollection Implementations](unsafemutablemidieventpacketpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](unsafemutablemidieventpacketpointer/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
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
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidieventpacketpointer)*