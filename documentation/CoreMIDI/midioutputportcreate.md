# MIDIOutputPortCreate(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates an output port through which a client sends outgoing MIDI messages to any MIDI destination.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIOutputPortCreate(_ client: MIDIClientRef, _ portName: CFString, _ outPort: UnsafeMutablePointer<MIDIPortRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Output ports provide a mechanism for MIDI merging. Core MIDI assumes that each output port is responsible for sending only a single MIDI stream to each destination, although a single port may address all of the destinations in the system.

Multiple output ports are only necessary when an application is capable of directing multiple simultaneous MIDI streams to the same destination.

## Parameters

- `client`: The client to own the newly created port.
- `portName`: The name of the port.
- `outPort`: On successful return, points to the newly created port.

## See Also

- [func MIDIInputPortCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIPortRef>, MIDIReceiveBlock) -> OSStatus](midiinputportcreatewithprotocol(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
- [func MIDIPortDispose(MIDIPortRef) -> OSStatus](midiportdispose(_:).md)
  Disposes of a MIDI port.
- [func MIDIPortConnectSource(MIDIPortRef, MIDIEndpointRef, UnsafeMutableRawPointer?) -> OSStatus](midiportconnectsource(_:_:_:).md)
  Makes a connection from a source to a client input port.
- [func MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus](midiportdisconnectsource(_:_:).md)
  Closes a previously established source-to-input port connection.
- [typealias MIDIPortRef](midiportref.md)
  A MIDI connection that a client maintains.
- [typealias MIDIReceiveBlock](midireceiveblock.md)
  A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midioutputportcreate(_:_:_:))*