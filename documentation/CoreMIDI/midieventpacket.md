# MIDIEventPacket

**Framework**: Core MIDI  
**Kind**: struct

A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.

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
struct MIDIEventPacket
```

## Topics

### Configuring an Event Packet
- [var timeStamp: MIDITimeStamp](midieventpacket/timestamp.md)
  The event packet timestamp.
- [var wordCount: UInt32](midieventpacket/wordcount.md)
  The number of valid MIDI 32-bit words in this event packet.
- [var words: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](midieventpacket/words.md)
  A variable-length stream of native-endian 32-bit Universal MIDI Packets (UMP).
### Classes
- [MIDIEventPacket.Builder](midieventpacket/builder.md)
### Structures
- [MIDIEventPacket.WordCollection](midieventpacket/wordcollection.md)
- [MIDIEventPacket.WordSequence](midieventpacket/wordsequence.md)
### Initializers
- [init()](midieventpacket/init.md)
- [init(timeStamp: MIDITimeStamp, wordCount: UInt32, words: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))](midieventpacket/init(timestamp:wordcount:words:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacket)*