# MIDIReceivedEventList(_:_:)

**Framework**: Core MIDI  
**Kind**: func

Distributes incoming MIDI events from a source to its connected client input ports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIReceivedEventList(_ src: MIDIEndpointRef, _ evtlist: UnsafePointer<MIDIEventList>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers can call this function when receiving MIDI events from a source.

Clients that create virtual sources, using [`MIDISourceCreateWithProtocol(_:_:_:_:)`](midisourcecreatewithprotocol(_:_:_:_:).md), can call this function when the source is generating MIDI events.

## Parameters

- `src`: The source that’s transmitting MIDI events.
- `evtlist`: The MIDI events to transmit.

## See Also

- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistinit(_:_:).md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistadd(_:_:_:_:_:_:).md)
  Adds an event to an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventpacketnext(_:).md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
- [func MIDISendEventList(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midisendeventlist(_:_:_:).md)
  Sends MIDI events to a destination.
- [struct MIDIEventList](midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireceivedeventlist(_:_:))*