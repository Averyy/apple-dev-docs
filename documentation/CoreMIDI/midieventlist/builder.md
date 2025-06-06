# MIDIEventList.Builder

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
- [init(inProtocol: MIDIProtocolID, wordSize: Int)](midieventlist/builder/init(inprotocol:wordsize:).md)
### Instance Properties
- [var count: Int](midieventlist/builder/count.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, words: [UInt32]) -> UnsafePointer<MIDIEventPacket>?](midieventlist/builder/append(timestamp:words:).md)
- [func clear()](midieventlist/builder/clear.md)
- [func withUnsafeMutableMIDIEventListPointer<Result>((inout UnsafeMutableMIDIEventListPointer) -> Result) -> Result](midieventlist/builder/withunsafemutablemidieventlistpointer(_:).md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIEventList>) -> Result) -> Result](midieventlist/builder/withunsafepointer(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlist/builder)*