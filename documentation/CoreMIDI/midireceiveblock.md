# MIDIReceiveBlock

**Framework**: Core MIDI  
**Kind**: typealias

A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias MIDIReceiveBlock = (UnsafePointer<MIDIEventList>, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

A client receives incoming MIDI messages through this callback block.

The [`MIDIInputPortCreateWithProtocol(_:_:_:_:_:)`](midiinputportcreatewithprotocol(_:_:_:_:_:).md) and [`MIDIDestinationCreateWithProtocol(_:_:_:_:_:)`](mididestinationcreatewithprotocol(_:_:_:_:_:).md) functions receive a [`MIDIReceiveBlock`](midireceiveblock.md). The system creates a high-priority receive thread on your client’s behalf, and from that thread it calls your [`MIDIReceiveBlock`](midireceiveblock.md) when incoming MIDI messages arrive.

## Parameters

- `evtlist`: The incoming MIDI message(s).
- `srcConnRefCon`: The refCon that identifies the source of the data, which is the value that you pass for the   parameter to  . This value is always   when receiving a MIDI event on a virtual input.

## See Also

- [func MIDIInputPortCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIPortRef>, MIDIReceiveBlock) -> OSStatus](midiinputportcreatewithprotocol(_:_:_:_:_:).md)
  Creates an input port through which the client may receive incoming MIDI messages from any MIDI source.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireceiveblock)*