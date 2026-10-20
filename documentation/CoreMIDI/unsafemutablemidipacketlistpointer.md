# UnsafeMutableMIDIPacketListPointer

**Framework**: Core MIDI  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS

## Declaration

```swift
struct UnsafeMutableMIDIPacketListPointer
```

## Topics

### Initializers
- [init(UnsafeMutablePointer<MIDIPacketList>, byteSize: Int)](./unsafemutablemidipacketlistpointer/init%28_,bytesize%29-8acwt.md)
- [init?(UnsafeMutablePointer<MIDIPacketList>?, byteSize: Int)](./unsafemutablemidipacketlistpointer/init%28_,bytesize%29-96k5n.md)
### Instance Properties
- [var count: Int](./unsafemutablemidipacketlistpointer/count.md)
- [var lastPacket: UnsafeMutablePointer<MIDIPacket>?](./unsafemutablemidipacketlistpointer/lastpacket.md)
- [var listSizeInBytes: Int](./unsafemutablemidipacketlistpointer/listsizeinbytes.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, data: [UInt8]) -> UnsafePointer<MIDIPacket>?](./unsafemutablemidipacketlistpointer/append%28timestamp,data%29.md)
- [func clear()](./unsafemutablemidipacketlistpointer/clear%28%29.md)

## Relationships

### Conforms To
- [Sequence](../Swift/sequence.md)

## See Also

### Packet list management
- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](./midipacketnext%28_%29.md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](./midipacket.md)
  A collection of simultaneous MIDI events.
- [struct MIDIPacketList](./midipacketlist.md)
  A list of MIDI events the system sends to or receives from an endpoint.
- [typealias MIDITimeStamp](./miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketPointer](./unsafemutablemidipacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidipacketlistpointer)*