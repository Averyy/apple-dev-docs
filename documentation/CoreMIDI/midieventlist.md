# MIDIEventList

**Framework**: Core MIDI  
**Kind**: struct

A variable-length list of MIDI event packets.

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
struct MIDIEventList
```

## Topics

### Configuring an Event List
- [var `protocol`: MIDIProtocolID](midieventlist/protocol.md)
  The MIDI protocol variant of the events in the list.
- [var numPackets: UInt32](midieventlist/numpackets.md)
  The number of MIDI event packet structures in the list.
- [var packet: MIDIEventPacket](midieventlist/packet.md)
  An array of variable-length MIDI event packet structures.
### Classes
- [MIDIEventList.Builder](midieventlist/builder.md)
### Structures
- [MIDIEventList.UnsafeSequence](midieventlist/unsafesequence.md)
### Initializers
- [init()](midieventlist/init.md)
- [init(protocol: MIDIProtocolID, numPackets: UInt32, packet: MIDIEventPacket)](midieventlist/init(protocol:numpackets:packet:).md)
### Type Methods
- [static func sizeInBytes(pktList: UnsafePointer<MIDIEventList>) -> Int](midieventlist/sizeinbytes(pktlist:).md)

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
- [struct MIDIEventPacket](midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlist)*