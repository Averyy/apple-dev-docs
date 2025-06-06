# MIDIPortConnectSource(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Makes a connection from a source to a client input port.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIPortConnectSource(_ port: MIDIPortRef, _ source: MIDIEndpointRef, _ connRefCon: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `port`: The port on which to create the connection.
- `source`: The source from which to create the connection.
- `connRefCon`: The data that passes to the port’s   to identify the source, which is always   for virtual destinations.

## See Also

- [func MIDIInputPortCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIPortRef>, MIDIReceiveBlock) -> OSStatus](midiinputportcreatewithprotocol(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIOutputPortCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](midioutputportcreate(_:_:_:).md)
  Creates an output port through which a client sends outgoing MIDI messages to any MIDI destination.
- [func MIDIPortDispose(MIDIPortRef) -> OSStatus](midiportdispose(_:).md)
  Disposes of a MIDI port.
- [func MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus](midiportdisconnectsource(_:_:).md)
  Closes a previously established source-to-input port connection.
- [typealias MIDIPortRef](midiportref.md)
  A MIDI connection that a client maintains.
- [typealias MIDIReceiveBlock](midireceiveblock.md)
  A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiportconnectsource(_:_:_:))*