# velocity

**Framework**: AVFAudio  
**Kind**: property

The MDI velocity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var velocity: Float { get set }
```

#### Discussion

If the instrument in the [`AVMusicTrack`](avmusictrack.md) destination audio unit supports fractional values, use this to generate precise changes in gain and other values. The valid range of values depend on the destination audio unit, and is usually between `0.0` and `127.0`.

## See Also

- [var midiNote: Float](avextendednoteonevent/midinote.md)
  The MIDI note number.
- [var instrumentID: UInt32](avextendednoteonevent/instrumentid.md)
  The instrument identifier.
- [var groupID: UInt32](avextendednoteonevent/groupid.md)
  The audio unit channel that handles the event.
- [var duration: AVMusicTimeStamp](avextendednoteonevent/duration.md)
  The duration of the event, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent/velocity)*