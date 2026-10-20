# MIDIPacketList.Builder

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
- [init(byteSize: Int)](./builder/init%28bytesize%29.md)
### Instance Properties
- [var count: Int](./builder/count.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, data: [UInt8]) -> UnsafePointer<MIDIPacket>?](./builder/append%28timestamp,data%29.md)
- [func clear()](./builder/clear%28%29.md)
- [func withUnsafeMutableMIDIPacketListPointer<Result>((inout UnsafeMutableMIDIPacketListPointer) -> Result) -> Result](./builder/withunsafemutablemidipacketlistpointer%28_%29.md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIPacketList>) -> Result) -> Result](./builder/withunsafepointer%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketlist/builder)*