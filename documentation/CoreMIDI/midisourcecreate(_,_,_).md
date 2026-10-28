# MIDISourceCreate(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Creates a virtual source in a client.

**Availability**:
- iOS 4.2+ - Deprecated in 27.2 (renamed: MIDISourceCreateWithProtocol(_:_:_:_:))
- iPadOS 4.2+ - Deprecated in 27.2 (renamed: MIDISourceCreateWithProtocol(_:_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: MIDISourceCreateWithProtocol(_:_:_:_:))
- macOS 10.0+ - Deprecated in 27.2 (renamed: MIDISourceCreateWithProtocol(_:_:_:_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MIDISourceCreateWithProtocol(_:_:_:_:))

> **Deprecated**: Use [`MIDISourceCreateWithProtocol(_:_:_:_:)`](./midisourcecreatewithprotocol%28_,_,_,_%29.md) instead.

## Declaration

```swift
func MIDISourceCreate(_ client: MIDIClientRef, _ name: CFString, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus
```

```c
extern OSStatus MIDISourceCreate(MIDIClientRef client, CFStringRef name, MIDIEndpointRef *outSrc);
```

## Return Value

An OSStatus result code.

## Discussion

Drivers need not call this; when they create devices and entities, sources and destinations are created at that time.

After creating a virtual source, use MIDIReceived to transmit MIDI messages from your virtual source to any clients connected to the virtual source.

After creating a virtual source, it’s a good idea to assign it the same unique ID it had the last time your application created it. (Although you should be prepared for this to fail in the unlikely event of a collision.) This will permit other clients to retain persistent references to your virtual source more easily.

## Parameters

- `client`: The client owning the virtual source.
- `name`: The name of the virtual source.
- `outSrc`: On successful return, a pointer to the newly-created source.

## See Also

### Deprecated Functions
- [func MIDIInputPortCreate(MIDIClientRef, CFString, MIDIReadProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](./midiinputportcreate%28_,_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIInputPortCreateWithBlock(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>, MIDIReadBlock) -> OSStatus](./midiinputportcreatewithblock%28_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisourcecreate(_:_:_:))*