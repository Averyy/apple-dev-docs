# MIDIInputPortCreateWithBlock(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: @escaping MIDIReadBlock) -> OSStatus
```

#### Return Value

An OSStatus result code.

#### Discussion

After creating a port, use MIDIPortConnectSource to establish an input connection from any number of sources to your port.

readBlock will be called on a separate high-priority thread owned by CoreMIDI.

## Parameters

- `client`: The client to own the newly-created port.
- `portName`: The name of the port.
- `outPort`: On successful return, points to the newly-created MIDIPort.
- `readBlock`: The MIDIReadBlock which will be called with incoming MIDI, from sources connected to this port.

## See Also

- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](midiinputportcreate(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDISourceCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](midisourcecreate(_:_:_:).md)
  Creates a virtual source in a client.
- [func MIDIDestinationCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](mididestinationcreate(_:_:_:_:_:).md)
  Creates a virtual destination in a client.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiinputportcreatewithblock(_:_:_:_:))*