# UnsafeMutableMIDIPacketPointer

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
struct UnsafeMutableMIDIPacketPointer
```

## Topics

### Initializers
- [init(UnsafeMutablePointer<MIDIPacket>)](./unsafemutablemidipacketpointer/init%28_%29-5z9po.md)
- [init?(UnsafeMutablePointer<MIDIPacket>?)](./unsafemutablemidipacketpointer/init%28_%29-7ypj1.md)
### Instance Properties
- [var count: Int](./unsafemutablemidipacketpointer/count.md)
- [var timeStamp: Int](./unsafemutablemidipacketpointer/timestamp.md)
### Default Implementations
- [MutableCollection Implementations](./unsafemutablemidipacketpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](./unsafemutablemidipacketpointer/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
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
- [struct UnsafeMutableMIDIPacketListPointer](./unsafemutablemidipacketlistpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidipacketpointer)*