# MIDIPortRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A MIDI connection that a client maintains.

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
typealias MIDIPortRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIPortRef;
```

## Discussion

A port object derives from [`MIDIObjectRef`](./midiobjectref.md), and its owning object is a [`MIDIDeviceRef`](./midideviceref.md). It represents an input or output port, and it provides the means to communicate with any number of MIDI sources or destinations.

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
- [typealias MIDIReceiveBlock](./midireceiveblock.md)
  A block receiving MIDI input that includes the incoming messages and a refCon to identify the source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiportref)*