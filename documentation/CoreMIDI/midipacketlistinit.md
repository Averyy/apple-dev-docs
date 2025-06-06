# MIDIPacketListInit(_:)

**Framework**: Core MIDI  
**Kind**: func

Prepares a MIDIPacketList to be built up dynamically.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIPacketListInit(_ pktlist: UnsafeMutablePointer<MIDIPacketList>) -> UnsafeMutablePointer<MIDIPacket>
```

#### Return Value

A pointer to the first MIDIPacket in the packet list.

## Parameters

- `pktlist`: The packet list to be initialized.

## See Also

- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](midiinputportcreate(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIInputPortCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>, MIDIReadBlock) -> OSStatus](midiinputportcreatewithblock(_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDISourceCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](midisourcecreate(_:_:_:).md)
  Creates a virtual source in a client.
- [func MIDIDestinationCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](mididestinationcreate(_:_:_:_:_:).md)
  Creates a virtual destination in a client.
- [func MIDIDestinationCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReadBlock) -> OSStatus](mididestinationcreatewithblock(_:_:_:_:).md)
  Creates a virtual destination in a client.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlistinit(_:))*