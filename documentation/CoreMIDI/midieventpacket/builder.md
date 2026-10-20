# MIDIEventPacket.Builder

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS

## Declaration

```swift
class Builder
```

## Topics

### Initializers
- [init(maximumNumberMIDIWords: Int)](./builder/init%28maximumnumbermidiwords%29.md)
### Instance Properties
- [var capacity: Int](./builder/capacity.md)
- [var count: Int](./builder/count.md)
- [var timeStamp: Int](./builder/timestamp.md)
### Instance Methods
- [func append(UInt32...)](./builder/append%28_%29.md)
- [func withUnsafeMutableMIDIEventPacketPointer<Result>((inout UnsafeMutableMIDIEventPacketPointer) -> Result) -> Result](./builder/withunsafemutablemidieventpacketpointer%28_%29.md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIEventPacket>) -> Result) -> Result](./builder/withunsafepointer%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacket/builder)*