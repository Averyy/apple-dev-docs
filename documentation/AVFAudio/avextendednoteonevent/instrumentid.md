# instrumentID

**Framework**: AVFAudio  
**Kind**: property

The instrument identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var instrumentID: UInt32 { get set }
```

#### Discussion

Set this value to [`defaultInstrument`](avextendednoteonevent/defaultinstrument.md).

## See Also

- [var midiNote: Float](avextendednoteonevent/midinote.md)
  The MIDI note number.
- [var velocity: Float](avextendednoteonevent/velocity.md)
  The MDI velocity.
- [var groupID: UInt32](avextendednoteonevent/groupid.md)
  The audio unit channel that handles the event.
- [var duration: AVMusicTimeStamp](avextendednoteonevent/duration.md)
  The duration of the event, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/instrumentid)*