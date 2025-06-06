# UnsafeMutableMIDIPacketPointer

**Framework**: Core MIDI  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct UnsafeMutableMIDIPacketPointer
```

## Topics

### Initializers
- [init(UnsafeMutablePointer<MIDIPacket>)](unsafemutablemidipacketpointer/init(_:)-5z9po.md)
- [init?(UnsafeMutablePointer<MIDIPacket>?)](unsafemutablemidipacketpointer/init(_:)-7ypj1.md)
### Instance Properties
- [var count: Int](unsafemutablemidipacketpointer/count.md)
- [var timeStamp: Int](unsafemutablemidipacketpointer/timestamp.md)
### Default Implementations
- [MutableCollection Implementations](unsafemutablemidipacketpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](unsafemutablemidipacketpointer/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](midipacketnext(_:).md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](midipacket.md)
  A collection of simultaneous MIDI events.
- [struct MIDIPacketList](midipacketlist.md)
  A list of MIDI events the system sends to or receives from an endpoint.
- [typealias MIDITimeStamp](miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketListPointer](unsafemutablemidipacketlistpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/unsafemutablemidipacketpointer)*