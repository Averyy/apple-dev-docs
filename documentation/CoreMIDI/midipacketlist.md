# MIDIPacketList

**Framework**: Core MIDI  
**Kind**: struct

A list of MIDI events the system sends to or receives from an endpoint.

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
struct MIDIPacketList
```

## Topics

### Inspecting a Packet List
- [var numPackets: UInt32](midipacketlist/numpackets.md)
  The number of MIDI packets in the list.
- [var packet: MIDIPacket](midipacketlist/packet.md)
  An open-ended array of variable-length MIDI packets.
### Classes
- [MIDIPacketList.Builder](midipacketlist/builder.md)
### Structures
- [MIDIPacketList.UnsafeSequence](midipacketlist/unsafesequence.md)
### Initializers
- [init()](midipacketlist/init.md)
- [init(numPackets: UInt32, packet: MIDIPacket)](midipacketlist/init(numpackets:packet:).md)
### Type Methods
- [static func sizeInBytes(pktList: UnsafePointer<MIDIPacketList>) -> Int](midipacketlist/sizeinbytes(pktlist:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](midipacketnext(_:).md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](midipacket.md)
  A collection of simultaneous MIDI events.
- [typealias MIDITimeStamp](miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketListPointer](unsafemutablemidipacketlistpointer.md)
- [struct UnsafeMutableMIDIPacketPointer](unsafemutablemidipacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlist)*