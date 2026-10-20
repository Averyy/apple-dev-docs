# MIDIPacketListAdd(_:_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Adds a MIDI event to a MIDIPacketList.

**Availability**:
- iOS 4.2+ - Deprecated in 27.2 (renamed: MIDIEventListAdd(_:_:_:_:_:_:))
- iPadOS 4.2+ - Deprecated in 27.2 (renamed: MIDIEventListAdd(_:_:_:_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDIEventListAdd(_:_:_:_:_:_:))
- macOS 10.0+ - Deprecated in 27.2 (renamed: MIDIEventListAdd(_:_:_:_:_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDIEventListAdd(_:_:_:_:_:_:))

> **Deprecated**: Use [`MIDIEventListAdd(_:_:_:_:_:_:)`](./midieventlistadd%28_,_,_,_,_,_%29.md) instead.

## Declaration

```swift
func MIDIPacketListAdd(_ pktlist: UnsafeMutablePointer<MIDIPacketList>, _ listSize: Int, _ curPacket: UnsafeMutablePointer<MIDIPacket>, _ time: MIDITimeStamp, _ nData: Int, _ data: UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket>
```

```c
extern MIDIPacket *MIDIPacketListAdd(MIDIPacketList *pktlist, ByteCount listSize, MIDIPacket *curPacket, MIDITimeStamp time, ByteCount nData, const Byte *data);
```

#### Return Value

Returns null if there was not room in the packet for the event; otherwise returns a packet pointer which should be passed as curPacket in a subsequent call to this function.

#### Discussion

The maximum size of a packet list is 65536 bytes. Large sysex messages must be sent in smaller packet lists.

## Parameters

- `pktlist`: The packet list to which the event is to be added.
- `listSize`: The size, in bytes, of the packet list.
- `curPacket`: A packet pointer returned by a previous call to MIDIPacketListInit or MIDIPacketListAdd for this packet list.
- `time`: The new event’s time.
- `nData`: The length of the new event, in bytes.
- `data`: The new event. May be a single MIDI event, or a partial sys-ex event. Running status is *not* permitted.

## See Also

### Deprecated Functions
- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](./midiinputportcreate%28_,_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIInputPortCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>, MIDIReadBlock) -> OSStatus](./midiinputportcreatewithblock%28_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDISourceCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](./midisourcecreate%28_,_,_%29.md)
  Creates a virtual source in a client.
- [func MIDIDestinationCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](./mididestinationcreate%28_,_,_,_,_%29.md)
  Creates a virtual destination in a client.
- [func MIDIDestinationCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReadBlock) -> OSStatus](./mididestinationcreatewithblock%28_,_,_,_%29.md)
  Creates a virtual destination in a client.
- [func MIDIPacketListInit(UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket>](./midipacketlistinit%28_%29.md)
  Prepares a MIDIPacketList to be built up dynamically.
- [func MIDISend(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./midisend%28_,_,_%29.md)
  Sends MIDI to a destination.
- [func MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./midireceived%28_,_%29.md)
  Distributes incoming MIDI from a source to the client input ports which are connected to that source.
- [typealias MIDIReadProc](./midireadproc.md)
  A function receiving MIDI input.
- [typealias MIDIReadBlock](./midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlistadd(_:_:_:_:_:_:))*