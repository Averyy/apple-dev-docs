# MIDIEventPacket.Builder

**Framework**: Core MIDI  
**Kind**: class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
class Builder
```

## Topics

### Initializers
- [init(maximumNumberMIDIWords: Int)](midieventpacket/builder/init(maximumnumbermidiwords:).md)
### Instance Properties
- [var capacity: Int](midieventpacket/builder/capacity.md)
- [var count: Int](midieventpacket/builder/count.md)
- [var timeStamp: Int](midieventpacket/builder/timestamp.md)
### Instance Methods
- [func append(UInt32...)](midieventpacket/builder/append(_:).md)
- [func withUnsafeMutableMIDIEventPacketPointer<Result>((inout UnsafeMutableMIDIEventPacketPointer) -> Result) -> Result](midieventpacket/builder/withunsafemutablemidieventpacketpointer(_:).md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIEventPacket>) -> Result) -> Result](midieventpacket/builder/withunsafepointer(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacket/builder)*