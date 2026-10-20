# MIDIPacketList

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A list of MIDI events the system sends to or receives from an endpoint.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct MIDIPacketList
```

```c
struct MIDIPacketList;
```

## Topics

### Inspecting a Packet List
- [var numPackets: UInt32](./midipacketlist/numpackets.md)
  The number of MIDI packets in the list.
- [var packet: MIDIPacket](./midipacketlist/packet.md)
  An open-ended array of variable-length MIDI packets.
### Classes
- [MIDIPacketList.Builder](./midipacketlist/builder.md)
### Structures
- [MIDIPacketList.UnsafeSequence](./midipacketlist/unsafesequence.md)
### Initializers
- [init()](./midipacketlist/init%28%29.md)
- [init(numPackets: UInt32, packet: MIDIPacket)](./midipacketlist/init%28numpackets,packet%29.md)
### Type Methods
- [static func sizeInBytes(pktList: UnsafePointer<MIDIPacketList>) -> Int](./midipacketlist/sizeinbytes%28pktlist%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Packet list management
- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](./midipacketnext%28_%29.md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](./midipacket.md)
  A collection of simultaneous MIDI events.
- [typealias MIDITimeStamp](./miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketListPointer](./unsafemutablemidipacketlistpointer.md)
- [struct UnsafeMutableMIDIPacketPointer](./unsafemutablemidipacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlist)*