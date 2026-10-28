# MIDIEventListInit(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Initializes an event list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func MIDIEventListInit(_ evtlist: UnsafeMutablePointer<MIDIEventList>, _ protocol: MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>
```

```c
extern MIDIEventPacket *MIDIEventListInit(MIDIEventList *evtlist, MIDIProtocolID protocol);
```

## Return Value

A pointer to the first [`MIDIEventPacket`](./midieventpacket.md) in the event list.

## Parameters

- `evtlist`: The event list to initialize.
- `protocol`: The MIDI protocol variant.

## See Also

### Event list management
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
- [struct UnsafeMutableMIDIEventListPointer](./unsafemutablemidieventlistpointer.md)
- [struct UnsafeMutableMIDIEventPacketPointer](./unsafemutablemidieventpacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlistinit(_:_:))*