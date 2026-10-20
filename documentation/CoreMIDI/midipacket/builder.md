# MIDIPacket.Builder

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS

## Declaration

```swift
class Builder
```

## Topics

### Initializers
- [init(maximumNumberMIDIBytes: Int)](./builder/init%28maximumnumbermidibytes%29.md)
### Instance Properties
- [var capacity: Int](./builder/capacity.md)
- [var count: Int](./builder/count.md)
- [var timeStamp: Int](./builder/timestamp.md)
### Instance Methods
- [func append(UInt8...)](./builder/append%28_%29.md)
- [func withUnsafeMutableMIDIPacketPointer<Result>((inout UnsafeMutableMIDIPacketPointer) -> Result) -> Result](./builder/withunsafemutablemidipacketpointer%28_%29.md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIPacket>) -> Result) -> Result](./builder/withunsafepointer%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacket/builder)*