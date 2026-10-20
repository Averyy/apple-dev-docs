# AVMusicTrackLoopCount

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Options that define the number of times a track loops.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVMusicTrackLoopCount
```

```c
enum AVMusicTrackLoopCount : NSInteger;
```

## Topics

### Creating a loop count
- [init?(rawValue: Int)](./avmusictrackloopcount/init%28rawvalue%29.md)
### Looping indefinitely
- [AVMusicTrackLoopCount.forever](./avmusictrackloopcount/forever.md)
  A track that loops forever.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling music tracks
- [class AVMusicTrack](./avmusictrack.md)
  A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [func createAndAppendTrack() -> AVMusicTrack](./avaudiosequencer/createandappendtrack%28%29.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func reverseEvents()](./avaudiosequencer/reverseevents%28%29.md)
  Reverses the order of all events in all music tracks, including the tempo track.
- [func removeTrack(AVMusicTrack) -> Bool](./avaudiosequencer/removetrack%28_%29.md)
  Removes the music track from the sequencer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrackloopcount)*