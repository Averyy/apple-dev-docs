# MIDIReceiveBlock

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias MIDIReceiveBlock = (UnsafePointer<MIDIEventList>, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (^)(const struct MIDIEventList *, void *) __attribute__((nonblocking)) MIDIReceiveBlock;
```

## Discussion

A client receives incoming MIDI messages through this callback block.

The [`MIDIInputPortCreateWithProtocol(_:_:_:_:_:)`](./midiinputportcreatewithprotocol%28_,_,_,_,_%29.md) and [`MIDIDestinationCreateWithProtocol(_:_:_:_:_:)`](./mididestinationcreatewithprotocol%28_,_,_,_,_%29.md) functions receive a [`MIDIReceiveBlock`](./midireceiveblock.md). The system creates a high-priority receive thread on your client’s behalf, and from that thread it calls your [`MIDIReceiveBlock`](./midireceiveblock.md) when incoming MIDI messages arrive.

## Parameters

- `evtlist`: The incoming MIDI message(s).
- `srcConnRefCon`: The refCon that identifies the source of the data, which is the value that you pass for the `connRefCon` parameter to [`MIDIPortConnectSource(_:_:_:)`](./midiportconnectsource%28_,_,_%29.md). This value is always [`nil`](../ObjectiveC/nil-227m0.md) when receiving a MIDI event on a virtual input.

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
- [func MIDIPortDisconnectSource(MIDIPortRef, MIDIEndpointRef) -> OSStatus](./midiportdisconnectsource%28_,_%29.md)
  Closes a previously established source-to-input port connection.
- [typealias MIDIPortRef](./midiportref.md)
  A MIDI connection that a client maintains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midireceiveblock)*