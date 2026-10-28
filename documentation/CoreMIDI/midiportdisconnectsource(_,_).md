# MIDIPortDisconnectSource(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Closes a previously established source-to-input port connection.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIPortDisconnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef) -> OSStatus
```

```c
extern OSStatus MIDIPortDisconnectSource(MIDIPortRef port, MIDIEndpointRef source);
```

## Return Value

An `OSStatus` result code.

## Parameters

- `port`: The port with the connection to close.
- `source`: The source from which to close a connection to a port.

## See Also

### Port management
- [func MIDIInputPortCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIPortRef>, MIDIReceiveBlock) -> OSStatus](./midiinputportcreatewithprotocol%28_,_,_,_,_%29.md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIOutputPortCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](./midioutputportcreate%28_,_,_%29.md)
  Creates an output port through which a client sends outgoing MIDI messages to any MIDI destination.
- [func MIDIPortDispose(MIDIPortRef) -> OSStatus](./midiportdispose%28_%29.md)
  Disposes of a MIDI port.
- [func MIDIPortConnectSource(MIDIPortRef, MIDIEndpointRef, UnsafeMutableRawPointer?) -> OSStatus](./midiportconnectsource%28_,_,_%29.md)
  Makes a connection from a source to a client input port.
- [typealias MIDIPortRef](./midiportref.md)
  A MIDI connection that a client maintains.
- [typealias MIDIReceiveBlock](./midireceiveblock.md)
  A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiportdisconnectsource(_:_:))*