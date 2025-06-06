# copyEvents(in:from:insertAt:)

**Framework**: AVFAudio  
**Kind**: method

Copies the events from the source track and splices them into the current music track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func copyEvents(in range: AVBeatRange, from sourceTrack: AVMusicTrack, insertAt insertStartBeat: AVMusicTimeStamp)
```

#### Discussion

All events originally at or past the insertion beat shift forward by the duration of the copied-in range.

## Parameters

- `range`: The range of beats.
- `sourceTrack`: The music track to copy the events from.
- `insertStartBeat`: The start beat to splice the events into.

## See Also

- [func cutEvents(in: AVBeatRange)](avmusictrack/cutevents(in:).md)
  Splices all events in the beat range from the music track.
- [func copyAndMergeEvents(in: AVBeatRange, from: AVMusicTrack, mergeAt: AVMusicTimeStamp)](avmusictrack/copyandmergeevents(in:from:mergeat:).md)
  Copies the events from the source track and merges them into the current music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/copyevents(in:from:insertat:))*