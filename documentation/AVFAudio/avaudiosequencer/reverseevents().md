# reverseEvents()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Reverses the order of all events in all music tracks, including the tempo track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func reverseEvents()
```

```objc
- (void) reverseEvents;
```

## See Also

### Handling music tracks
- [class AVMusicTrack](../avmusictrack.md)
  A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [func createAndAppendTrack() -> AVMusicTrack](./createandappendtrack%28%29.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func removeTrack(AVMusicTrack) -> Bool](./removetrack%28_%29.md)
  Removes the music track from the sequencer.
- [enum AVMusicTrackLoopCount](../avmusictrackloopcount.md)
  Options that define the number of times a track loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/reverseevents())*