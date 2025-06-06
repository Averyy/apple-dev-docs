# MIDIDestinationCreate(_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates a virtual destination in a client.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDestinationCreate(_ client: MIDIClientRef, _ name: CFString, _ readProc: MIDIReadProc, _ refCon: UnsafeMutableRawPointer?, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus
```

#### Return Value

An OSStatus result code.

#### Discussion

The specified readProc gets called when clients send MIDI to your virtual destination.

Drivers need not call this; when they create devices and entities, sources and destinations are created at that time.

After creating a virtual destination, it’s a good idea to assign it the same unique ID it had the last time your application created it. (Although you should be prepared for this to fail in the unlikely event of a collision.) This will permit other clients to retain persistent references to your virtual destination more easily.

See the discussion of kMIDIPropertyAdvanceScheduleTimeMuSec for notes about the relationship between when a sender sends MIDI to the destination and when it is received.

## Parameters

- `client`: The client owning the virtual destination.
- `name`: The name of the virtual destination.
- `readProc`: The MIDIReadProc to be called when a client sends MIDI to the virtual destination.
- `refCon`: The refCon to be passed to the readProc.
- `outDest`: On successful return, a pointer to the newly-created destination.

## See Also

- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](midiinputportcreate(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIInputPortCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>, MIDIReadBlock) -> OSStatus](midiinputportcreatewithblock(_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDISourceCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](midisourcecreate(_:_:_:).md)
  Creates a virtual source in a client.
- [func MIDIDestinationCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReadBlock) -> OSStatus](mididestinationcreatewithblock(_:_:_:_:).md)
  Creates a virtual destination in a client.
- [func MIDIPacketListInit(UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket>](midipacketlistinit(_:).md)
  Prepares a MIDIPacketList to be built up dynamically.
- [func MIDIPacketListAdd(UnsafeMutablePointer<MIDIPacketList>, Int, UnsafeMutablePointer<MIDIPacket>, MIDITimeStamp, Int, UnsafePointer<UInt8>) -> UnsafeMutablePointer<MIDIPacket>](midipacketlistadd(_:_:_:_:_:_:).md)
  Adds a MIDI event to a MIDIPacketList.
- [func MIDISend(MIDIPortRef, MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](midisend(_:_:_:).md)
  Sends MIDI to a destination.
- [func MIDIReceived(MIDIEndpointRef, UnsafePointer<MIDIPacketList>) -> OSStatus](midireceived(_:_:).md)
  Distributes incoming MIDI from a source to the client input ports which are connected to that source.
- [typealias MIDIReadProc](midireadproc.md)
  A function receiving MIDI input.
- [typealias MIDIReadBlock](midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididestinationcreate(_:_:_:_:_:))*