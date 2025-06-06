# timeStamp

**Framework**: Core MIDI  
**Kind**: property

The event packet timestamp.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var timeStamp: MIDITimeStamp
```

#### Discussion

If receiving MIDI data, this property represents the time at which the events occurred. If sending MIDI data, it represents the time at which to play the events. A value of 0 means “now.”

The time stamp applies to the first byte or word in the packet.

## See Also

- [var wordCount: UInt32](midieventpacket/wordcount.md)
  The number of valid MIDI 32-bit words in this event packet.
- [var words: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)](midieventpacket/words.md)
  A variable-length stream of native-endian 32-bit Universal MIDI Packets (UMP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midieventpacket/timestamp)*