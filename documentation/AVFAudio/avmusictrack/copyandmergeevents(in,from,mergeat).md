# copyAndMergeEvents(in:from:mergeAt:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Copies the events from the source track and merges them into the current music track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func copyAndMergeEvents(in range: AVBeatRange, from sourceTrack: AVMusicTrack, mergeAt mergeStartBeat: AVMusicTimeStamp)
```

```objc
- (void) copyAndMergeEventsInRange:(AVBeatRange) range fromTrack:(AVMusicTrack *) sourceTrack mergeAtBeat:(AVMusicTimeStamp) mergeStartBeat;
```

## Discussion

The system won’t modify events originally at or past the start beat. Copying events from track to track follows the same type-exclusion rules as adding events.

## Parameters

- `range`: The range of beats.
- `sourceTrack`: The music track to copy the events from.
- `mergeStartBeat`: The start beat where the copied events merge into.

## See Also

### Cutting and copying events
- [func cutEvents(in: AVBeatRange)](./cutevents%28in%29.md)
  Splices all events in the beat range from the music track.
- [func copyEvents(in: AVBeatRange, from: AVMusicTrack, insertAt: AVMusicTimeStamp)](./copyevents%28in,from,insertat%29.md)
  Copies the events from the source track and splices them into the current music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/copyandmergeevents(in:from:mergeat:))*