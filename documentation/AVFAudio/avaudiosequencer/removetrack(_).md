# removeTrack(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Removes the music track from the sequencer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func removeTrack(_ track: AVMusicTrack) -> Bool
```

```objc
- (BOOL) removeTrack:(AVMusicTrack *) track;
```

## Return Value

A Boolean value that indicates whether the call succeeds.

## Discussion

This method doesn’t destroy the method track since you can reuse it.

## Parameters

- `track`: The music track to remove.

## See Also

### Handling music tracks
- [class AVMusicTrack](../avmusictrack.md)
  A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [func createAndAppendTrack() -> AVMusicTrack](./createandappendtrack%28%29.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func reverseEvents()](./reverseevents%28%29.md)
  Reverses the order of all events in all music tracks, including the tempo track.
- [enum AVMusicTrackLoopCount](../avmusictrackloopcount.md)
  Options that define the number of times a track loops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/removetrack(_:))*