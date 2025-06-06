# MIDIEventPacketNext(_:)

**Framework**: Core MIDI  
**Kind**: func

Advances a packet pointer to the next packet in memory, if the packet is part of an event list.

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
func MIDIEventPacketNext(_ pkt: UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>
```

#### Return Value

The subsequent packet in the event list.

## Parameters

- `pkt`: A pointer to a   in an event list.

## See Also

- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistinit(_:_:).md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistadd(_:_:_:_:_:_:).md)
  Adds an event to an event list.
- [func MIDISendEventList(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midisendeventlist(_:_:_:).md)
  Sends MIDI events to a destination.
- [func MIDIReceivedEventList(MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midireceivedeventlist(_:_:).md)
  Distributes incoming MIDI events from a source to its connected client input ports.
- [struct MIDIEventList](midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacketnext(_:))*