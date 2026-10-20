# words

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

A variable-length stream of native-endian 32-bit Universal MIDI Packets (UMP).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var words: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)
```

```c
UInt32 words[64];
```

## See Also

### Configuring an Event Packet
- [var timeStamp: MIDITimeStamp](./timestamp.md)
  The event packet timestamp.
- [var wordCount: UInt32](./wordcount.md)
  The number of valid MIDI 32-bit words in this event packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacket/words)*