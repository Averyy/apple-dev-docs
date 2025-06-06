# cutEvents(in:)

**Framework**: AVFAudio  
**Kind**: method

Splices all events in the beat range from the music track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func cutEvents(in range: AVBeatRange)
```

#### Discussion

All events past the end of the range you specify shift backward by the duration of the range.

## Parameters

- `range`: The range of beats.

## See Also

- [func copyEvents(in: AVBeatRange, from: AVMusicTrack, insertAt: AVMusicTimeStamp)](avmusictrack/copyevents(in:from:insertat:).md)
  Copies the events from the source track and splices them into the current music track.
- [func copyAndMergeEvents(in: AVBeatRange, from: AVMusicTrack, mergeAt: AVMusicTimeStamp)](avmusictrack/copyandmergeevents(in:from:mergeat:).md)
  Copies the events from the source track and merges them into the current music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/cutevents(in:))*