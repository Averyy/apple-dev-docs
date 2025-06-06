# MIDIInputPortCreateWithProtocol(_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIInputPortCreateWithProtocol(_ client: MIDIClientRef, _ portName: CFString, _ protocol: MIDIProtocolID, _ outPort: UnsafeMutablePointer<MIDIPortRef>, _ receiveBlock: @escaping MIDIReceiveBlock) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

After creating a port, use [`MIDIPortConnectSource(_:_:_:)`](midiportconnectsource(_:_:_:).md) to establish an input connection from any number of sources to your port.

The system calls the receive block on a separate high-priority thread owned by Core MIDI.

## Parameters

- `client`: The client to own the newly created port.
- `portName`: The name of the port.
- `protocol`: The MIDI protocol variant to deliver to this port. The system automatically converts messages from one protocol to another as needed.
- `outPort`: On successful return, points to the newly created MIDI port.
- `receiveBlock`: A callback block the system invokes with incoming MIDI from sources connected to this port.

## See Also

- [func MIDIOutputPortCreate(MIDIClientRef, CFString, UnsafeMutablePointer<MIDIPortRef>) -> OSStatus](midioutputportcreate(_:_:_:).md)
  Creates an output port through which a client sends outgoing MIDI messages to any MIDI destination.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiinputportcreatewithprotocol(_:_:_:_:_:))*