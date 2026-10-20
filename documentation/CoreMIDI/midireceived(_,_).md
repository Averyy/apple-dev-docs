# MIDIReceived(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Distributes incoming MIDI from a source to the client input ports which are connected to that source.

**Availability**:
- iOS 4.2+ - Deprecated in 27.2 (renamed: MIDIReceivedEventList(_:_:))
- iPadOS 4.2+ - Deprecated in 27.2 (renamed: MIDIReceivedEventList(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDIReceivedEventList(_:_:))
- macOS 10.0+ - Deprecated in 27.2 (renamed: MIDIReceivedEventList(_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDIReceivedEventList(_:_:))

> **Deprecated**: Use [`MIDIReceivedEventList(_:_:)`](./midireceivedeventlist%28_,_%29.md) instead.

## Declaration

```swift
func MIDIReceived(_ src: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus
```

```c
extern OSStatus MIDIReceived(MIDIEndpointRef src, const MIDIPacketList *pktlist);
```

#### Return Value

An OSStatus result code.

#### Discussion

Drivers should call this function when receiving MIDI from a source.

Clients which have created virtual sources, using MIDISourceCreate, should call this function when the source is generating MIDI.

Unlike MIDISend(), a timestamp of 0 is not equivalent to “now”; the driver or virtual source is responsible for putting proper timestamps in the packets.

## Parameters

- `src`: The source which is transmitting MIDI.
- `pktlist`: The MIDI events to be transmitted.

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
- [typealias MIDIReadProc](./midireadproc.md)
  A function receiving MIDI input.
- [typealias MIDIReadBlock](./midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireceived(_:_:))*