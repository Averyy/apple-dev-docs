# AVMusicTrackLoopCount

**Framework**: AVFAudio  
**Kind**: enum

Options that define the number of times a track loops.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVMusicTrackLoopCount
```

## Topics

### Elements
- [AVMusicTrackLoopCount.forever](avmusictrackloopcount/forever.md)
  A track that loops forever.
### Initializers
- [init?(rawValue: Int)](avmusictrackloopcount/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVMusicTrack](avmusictrack.md)
  A collection of music events that you can offset, set to a muted state, modify independently from other track events, and send to a specified destination.
- [func createAndAppendTrack() -> AVMusicTrack](avaudiosequencer/createandappendtrack.md)
  Creates a new music track and appends it to the sequencer’s list.
- [func reverseEvents()](avaudiosequencer/reverseevents.md)
  Reverses the order of all events in all music tracks, including the tempo track.
- [func removeTrack(AVMusicTrack) -> Bool](avaudiosequencer/removetrack(_:).md)
  Removes the music track from the sequencer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrackloopcount)*