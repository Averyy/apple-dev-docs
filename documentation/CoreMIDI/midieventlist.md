# MIDIEventList

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

A variable-length list of MIDI event packets.

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
struct MIDIEventList
```

```c
struct MIDIEventList;
```

## Topics

### Configuring an Event List
- [var `protocol`: MIDIProtocolID](./midieventlist/protocol.md)
  The MIDI protocol variant of the events in the list.
- [var numPackets: UInt32](./midieventlist/numpackets.md)
  The number of MIDI event packet structures in the list.
- [var packet: MIDIEventPacket](./midieventlist/packet.md)
  An array of variable-length MIDI event packet structures.
### Classes
- [MIDIEventList.Builder](./midieventlist/builder.md)
### Structures
- [MIDIEventList.UnsafeSequence](./midieventlist/unsafesequence.md)
### Initializers
- [init()](./midieventlist/init%28%29.md)
- [init(protocol: MIDIProtocolID, numPackets: UInt32, packet: MIDIEventPacket)](./midieventlist/init%28protocol,numpackets,packet%29.md)
### Type Methods
- [static func sizeInBytes(pktList: UnsafePointer<MIDIEventList>) -> Int](./midieventlist/sizeinbytes%28pktlist%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

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
- [struct MIDIEventPacket](./midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](./unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](./unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlist)*