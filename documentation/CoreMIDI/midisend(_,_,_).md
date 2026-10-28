# MIDISend(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Sends MIDI to a destination.

**Availability**:
- iOS 4.2+ - Deprecated in 27.2 (renamed: MIDISendEventList(_:_:_:))
- iPadOS 4.2+ - Deprecated in 27.2 (renamed: MIDISendEventList(_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDISendEventList(_:_:_:))
- macOS 10.0+ - Deprecated in 27.2 (renamed: MIDISendEventList(_:_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDISendEventList(_:_:_:))

> **Deprecated**: Use [`MIDISendEventList(_:_:_:)`](./midisendeventlist%28_,_,_%29.md) instead.

## Declaration

```swift
func MIDISend(_ port: MIDIPortRef, _ dest: MIDIEndpointRef, _ pktlist: UnsafePointer<MIDIPacketList>) -> OSStatus
```

```c
extern OSStatus MIDISend(MIDIPortRef port, MIDIEndpointRef dest, const MIDIPacketList *pktlist);
```

## Return Value

An OSStatus result code.

## Discussion

Events with future timestamps are scheduled for future delivery. CoreMIDI performs any needed MIDI merging.

## Parameters

- `port`: The output port through which the MIDI is to be sent.
- `dest`: The destination to receive the events.
- `pktlist`: The MIDI events to be sent.

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
- [func MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](./midireceived%28_,_%29.md)
  Distributes incoming MIDI from a source to the client input ports which are connected to that source.
- [typealias MIDIReadProc](./midireadproc.md)
  A function receiving MIDI input.
- [typealias MIDIReadBlock](./midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisend(_:_:_:))*