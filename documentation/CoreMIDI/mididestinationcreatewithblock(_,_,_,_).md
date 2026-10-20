# MIDIDestinationCreateWithBlock(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Creates a virtual destination in a client.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2 (renamed: MIDIDestinationCreateWithProtocol(_:_:_:_:_:))
- iPadOS 9.0+ - Deprecated in 27.2 (renamed: MIDIDestinationCreateWithProtocol(_:_:_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDIDestinationCreateWithProtocol(_:_:_:_:_:))
- macOS 10.11+ - Deprecated in 27.2 (renamed: MIDIDestinationCreateWithProtocol(_:_:_:_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDIDestinationCreateWithProtocol(_:_:_:_:_:))

> **Deprecated**: Use [`MIDIDestinationCreateWithProtocol(_:_:_:_:_:)`](./mididestinationcreatewithprotocol%28_,_,_,_,_%29.md) instead.

## Declaration

```swift
func MIDIDestinationCreateWithBlock(_ client: MIDIClientRef, _ name: CFString, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: @escaping MIDIReadBlock) -> OSStatus
```

```c
extern OSStatus MIDIDestinationCreateWithBlock(MIDIClientRef client, CFStringRef name, MIDIEndpointRef *outDest, MIDIReadBlock readBlock);
```

#### Return Value

An OSStatus result code.

#### Discussion

The specified readBlock gets called when clients send MIDI to your virtual destination.

Drivers need not call this; when they create devices and entities, sources and destinations are created at that time.

After creating a virtual destination, it’s a good idea to assign it the same unique ID it had the last time your application created it. (Although you should be prepared for this to fail in the unlikely event of a collision.) This will permit other clients to retain persistent references to your virtual destination more easily.

See the discussion of kMIDIPropertyAdvanceScheduleTimeMuSec for notes about the relationship between when a sender sends MIDI to the destination and when it is received.

## Parameters

- `client`: The client owning the virtual destination.
- `name`: The name of the virtual destination.
- `outDest`: On successful return, a pointer to the newly-created destination.
- `readBlock`: The MIDIReadBlock to be called when a client sends MIDI to the virtual destination.

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
- [typealias MIDIReadBlock](./midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididestinationcreatewithblock(_:_:_:_:))*