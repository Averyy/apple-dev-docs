# MIDIEventListAdd(_:_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Adds an event to an event list.

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
func MIDIEventListAdd(_ evtlist: UnsafeMutablePointer<MIDIEventList>, _ listSize: Int, _ curPacket: UnsafeMutablePointer<MIDIEventPacket>, _ time: MIDITimeStamp, _ wordCount: Int, _ words: UnsafePointer<UInt32>) -> UnsafeMutablePointer<MIDIEventPacket>
```

#### Return Value

A packet pointer to pass as the `curPacket` argument in a subsequent call to this function, or `NULL` if there wasn’t room in the packet for the event.

#### Discussion

The maximum size of an event list is 65,536 bytes. Send large SysEx messages in smaller event lists.

## Parameters

- `evtlist`: The event list to which to add the event.
- `listSize`: The event list’s capacity, in bytes.
- `curPacket`: A packet pointer returned by a previous call to   or   for this packet list.
- `time`: The new event’s time.
- `wordCount`: The number of valid MIDI 32-bit words.
- `words`: The new event, which may be a single MIDI event or a partial SysEx event.

## See Also

- [func MIDIEventListInit(UnsafeMutablePointer<MIDIEventList>, MIDIProtocolID) -> UnsafeMutablePointer<MIDIEventPacket>](midieventlistinit(_:_:).md)
  Initializes an event list.
- [func MIDIEventPacketNext(UnsafePointer<MIDIEventPacket>) -> UnsafeMutablePointer<MIDIEventPacket>](midieventpacketnext(_:).md)
  Advances a packet pointer to the next packet in memory, if the packet is part of an event list.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlistadd(_:_:_:_:_:_:))*