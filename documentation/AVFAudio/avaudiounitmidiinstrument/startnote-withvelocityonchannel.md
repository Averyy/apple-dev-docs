# startNote(_:withVelocity:onChannel:)

**Framework**: AVFAudio  
**Kind**: method

Sends a MIDI Note On event to the instrument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startNote(_ note: UInt8, withVelocity velocity: UInt8, onChannel channel: UInt8)
```

## Parameters

- `note`: The note number (key) to play. The valid range is   to  .
- `velocity`: Specifies the volume to play the note at. The valid range is   to  .
- `channel`: The channel number to send the event to. The valid range is   to  .

## See Also

- [func stopNote(UInt8, onChannel: UInt8)](avaudiounitmidiinstrument/stopnote(_:onchannel:).md)
  Sends a MIDI Note Off event to the instrument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/startnote(_:withvelocity:onchannel:))*