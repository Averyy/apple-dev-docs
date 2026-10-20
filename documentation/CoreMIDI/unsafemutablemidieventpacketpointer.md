# UnsafeMutableMIDIEventPacketPointer

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS

## Declaration

```swift
struct UnsafeMutableMIDIEventPacketPointer
```

## Topics

### Initializers
- [init(UnsafeMutablePointer<MIDIEventPacket>)](./unsafemutablemidieventpacketpointer/init%28_%29-2pp97.md)
- [init?(UnsafeMutablePointer<MIDIEventPacket>?)](./unsafemutablemidieventpacketpointer/init%28_%29-91lug.md)
### Instance Properties
- [var count: Int](./unsafemutablemidieventpacketpointer/count.md)
- [var timeStamp: Int](./unsafemutablemidieventpacketpointer/timestamp.md)
### Default Implementations
- [MutableCollection Implementations](./unsafemutablemidieventpacketpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](./unsafemutablemidieventpacketpointer/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Event list management
- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventlistinit%28_,_%29.md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventlistadd%28_,_,_,_,_,_%29.md)
  Adds an event to an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](./midieventpacketnext%28_%29.md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
- [func MIDISendEventList(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](./midisendeventlist%28_,_,_%29.md)
  Sends MIDI events to a destination.
- [func MIDIReceivedEventList(MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](./midireceivedeventlist%28_,_%29.md)
  Distributes incoming MIDI events from a source to its connected client input ports.
- [struct MIDIEventList](./midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](./midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](./unsafemutablemidieventlistpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidieventpacketpointer)*