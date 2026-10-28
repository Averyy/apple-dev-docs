# MIDIInputPortCreateWithBlock(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.

**Availability**:
- iOS 9.0+ - Deprecated in 27.2 (renamed: MIDIInputPortCreateWithProtocol(_:_:_:_:_:))
- iPadOS 9.0+ - Deprecated in 27.2 (renamed: MIDIInputPortCreateWithProtocol(_:_:_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDIInputPortCreateWithProtocol(_:_:_:_:_:))
- macOS 10.11+ - Deprecated in 27.2 (renamed: MIDIInputPortCreateWithProtocol(_:_:_:_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDIInputPortCreateWithProtocol(_:_:_:_:_:))

> **Deprecated**: Use [`MIDIInputPortCreateWithProtocol(_:_:_:_:_:)`](./midiinputportcreatewithprotocol%28_,_,_,_,_%29.md) intead.

## Declaration

```swift
func MIDIInputPortCreateWithBlock(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ readBlock: @escaping MIDIReadBlock) -> OSStatus
```

```c
extern OSStatus MIDIInputPortCreateWithBlock(MIDIClientRef client, CFStringRef portName, MIDIPortRef *outPort, MIDIReadBlock readBlock);
```

## Return Value

An OSStatus result code.

## Discussion

After creating a port, use MIDIPortConnectSource to establish an input connection from any number of sources to your port.

readBlock will be called on a separate high-priority thread owned by CoreMIDI.

## Parameters

- `client`: The client to own the newly-created port.
- `portName`: The name of the port.
- `outPort`: On successful return, points to the newly-created MIDIPort.
- `readBlock`: The MIDIReadBlock which will be called with incoming MIDI, from sources connected to this port.

## See Also

### Deprecated Functions
- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](./midiinputportcreate%28_,_,_,_,_%29.md)
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
- [typealias MIDIReadBlock](./midireadblock.md)
  A block receiving MIDI input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiinputportcreatewithblock(_:_:_:_:))*