# MIDIEventList.Builder

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
- [init(inProtocol: MIDIProtocolID, wordSize: Int)](./builder/init%28inprotocol,wordsize%29.md)
### Instance Properties
- [var count: Int](./builder/count.md)
### Instance Methods
- [func append(timestamp: MIDITimeStamp, words: [UInt32]) -> UnsafePointer<MIDIEventPacket>?](./builder/append%28timestamp,words%29.md)
- [func clear()](./builder/clear%28%29.md)
- [func withUnsafeMutableMIDIEventListPointer<Result>((inout UnsafeMutableMIDIEventListPointer) -> Result) -> Result](./builder/withunsafemutablemidieventlistpointer%28_%29.md)
- [func withUnsafePointer<Result>((UnsafePointer<MIDIEventList>) -> Result) -> Result](./builder/withunsafepointer%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventlist/builder)*