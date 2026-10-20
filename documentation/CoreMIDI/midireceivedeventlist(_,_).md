# MIDIReceivedEventList(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus MIDIReceivedEventList(MIDIEndpointRef src, const MIDIEventList *evtlist);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers can call this function when receiving MIDI events from a source.

Clients that create virtual sources, using [`MIDISourceCreateWithProtocol(_:_:_:_:)`](./midisourcecreatewithprotocol%28_,_,_,_%29.md), can call this function when the source is generating MIDI events.

## Parameters

- `src`: The source that’s transmitting MIDI events.
- `evtlist`: The MIDI events to transmit.

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
- [struct MIDIEventList](./midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](./midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](./unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](./unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireceivedeventlist(_:_:))*