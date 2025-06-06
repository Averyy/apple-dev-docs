# groupID

**Framework**: AVFAudio  
**Kind**: property

The audio unit channel that handles the event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var groupID: UInt32 { get set }
```

#### Discussion

The valid range of values are between `0` and `15`, but can be higher if the [`AVMusicTrack`](avmusictrack.md) destination audio unit supports more channels.

## See Also

- [var midiNote: Float](avextendednoteonevent/midinote.md)
  The MIDI note number.
- [var velocity: Float](avextendednoteonevent/velocity.md)
  The MDI velocity.
- [var instrumentID: UInt32](avextendednoteonevent/instrumentid.md)
  The instrument identifier.
- [var duration: AVMusicTimeStamp](avextendednoteonevent/duration.md)
  The duration of the event, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/groupid)*