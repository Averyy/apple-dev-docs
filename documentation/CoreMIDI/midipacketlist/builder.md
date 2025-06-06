# MIDIPacketList.Builder

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
- [init(byteSize: Int)](midipacketlist/builder/init(bytesize:).md)
### Instance Properties
- [var count: Int](midipacketlist/builder/count.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, data: [UInt8]) -> UnsafePointer<MIDIPacket>?](midipacketlist/builder/append(timestamp:data:).md)
- [func clear()](midipacketlist/builder/clear.md)
- [func withUnsafeMutableMIDIPacketListPointer<Result>((inout UnsafeMutableMIDIPacketListPointer) -> Result) -> Result](midipacketlist/builder/withunsafemutablemidipacketlistpointer(_:).md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIPacketList>) -> Result) -> Result](midipacketlist/builder/withunsafepointer(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlist/builder)*