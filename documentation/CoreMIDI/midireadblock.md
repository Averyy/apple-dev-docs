# MIDIReadBlock

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A block receiving MIDI input.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2
- iPadOS 9.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.11+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: use MIDIReceiveBlock and MIDIEventLists

## Declaration

```swift
typealias MIDIReadBlock = (UnsafePointer<MIDIPacketList>, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (^)(const struct MIDIPacketList *, void *) __attribute__((nonblocking)) MIDIReadBlock;
```

#### Discussion

This is a callback block through which a client receives incoming MIDI messages.

A MIDIReadBlock is passed to the MIDIInputPortCreateWithBlock and MIDIDestinationCreateWithBlock functions. The CoreMIDI framework will create a high-priority receive thread on your client’s behalf, and from that thread, your MIDIReadProc will be called when incoming MIDI messages arrive.

## Parameters

- `pktlist`: The incoming MIDI message(s).
- `srcConnRefCon`: A refCon you passed to MIDIPortConnectSource, which identifies the source of the data.

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
- [func MIDIPacketListAdd(UnsafeMutablePointer<MIDIPacketList>, Int, UnsafeMutablePointer<MIDIPacket>, MIDITimeStamp, Int, UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket>](./midipacketlistadd%28_,_,_,_,_,_%29.md)
  Adds a MIDI event to a MIDIPacketList.
- [func MIDISend(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./midisend%28_,_,_%29.md)
  Sends MIDI to a destination.
- [func MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./midireceived%28_,_%29.md)
  Distributes incoming MIDI from a source to the client input ports which are connected to that source.
- [typealias MIDIReadProc](./midireadproc.md)
  A function receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireadblock)*