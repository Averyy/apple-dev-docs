# MIDISendEventList(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Sends MIDI events to a destination.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDISendEventList(_ port: MIDIPortRef, _ dest: MIDIEndpointRef, _ evtlist: UnsafePointer<MIDIEventList>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

The system schedules events with future timestamps for future delivery. It performs any needed MIDI merging.

## Parameters

- `port`: The output port through which to send MIDI events.
- `dest`: The destination to receive the events.
- `evtlist`: The MIDI events to send.

## See Also

- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistinit(_:_:).md)
  Initializes an event list.
- [func MIDIEventListAdd(UnsafeMutablePointer<MIDIEventList>, Int, UnsafeMutablePointer<MIDIEventPacket>, MIDITimeStamp, Int, UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistadd(_:_:_:_:_:_:).md)
  Adds an event to an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventpacketnext(_:).md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
- [func MIDIReceivedEventList(MIDIEndpointRef, UnsafePointer<MIDIEventList>) -> OSStatus](midireceivedeventlist(_:_:).md)
  Distributes incoming MIDI events from a source to its connected client input ports.
- [struct MIDIEventList](midieventlist.md)
  A variable-length list of MIDI event packets.
- [struct MIDIEventPacket](midieventpacket.md)
  A series of simultaneous MIDI events in Universal MIDI Packets (UMP) format.
- [struct UnsafeMutableMIDIEventListPointer](unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisendeventlist(_:_:_:))*