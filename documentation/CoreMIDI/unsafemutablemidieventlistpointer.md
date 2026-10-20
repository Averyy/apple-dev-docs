# UnsafeMutableMIDIEventListPointer

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
struct UnsafeMutableMIDIEventListPointer
```

## Topics

### Initializers
- [init?(UnsafeMutablePointer<MIDIEventList>?, wordSize: Int)](./unsafemutablemidieventlistpointer/init%28_,wordsize%29.md)
- [init(UnsafeMutablePointer<MIDIEventList>, wordSize: Int, inProtocol: MIDIProtocolID)](./unsafemutablemidieventlistpointer/init%28_,wordsize,inprotocol%29.md)
### Instance Properties
- [var count: Int](./unsafemutablemidieventlistpointer/count.md)
- [var lastPacket: UnsafeMutablePointer<MIDIEventPacket>?](./unsafemutablemidieventlistpointer/lastpacket.md)
- [var listSizeInBytes: Int](./unsafemutablemidieventlistpointer/listsizeinbytes.md)
- [var midiProtocol: MIDIProtocolID](./unsafemutablemidieventlistpointer/midiprotocol.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, words: [UInt32]) -> UnsafePointer<MIDIEventPacket>?](./unsafemutablemidieventlistpointer/append%28timestamp,words%29.md)
- [func clear()](./unsafemutablemidieventlistpointer/clear%28%29.md)

## Relationships

### Conforms To
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
- [struct UnsafeMutableMIDIEventPacketPointer](./unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidieventlistpointer)*