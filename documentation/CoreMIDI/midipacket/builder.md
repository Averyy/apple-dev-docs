# MIDIPacket.Builder

**Framework**: Core MIDI  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
class Builder
```

## Topics

### Initializers
- [init(maximumNumberMIDIBytes: Int)](midipacket/builder/init(maximumnumbermidibytes:).md)
### Instance Properties
- [var capacity: Int](midipacket/builder/capacity.md)
- [var count: Int](midipacket/builder/count.md)
- [var timeStamp: Int](midipacket/builder/timestamp.md)
### Instance Methods
- [func append(UInt8...)](midipacket/builder/append(_:).md)
- [func withUnsafeMutableMIDIPacketPointer<Result>((inout UnsafeMutableMIDIPacketPointer) -> Result) -> Result](midipacket/builder/withunsafemutablemidipacketpointer(_:).md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIPacket>) -> Result) -> Result](midipacket/builder/withunsafepointer(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacket/builder)*