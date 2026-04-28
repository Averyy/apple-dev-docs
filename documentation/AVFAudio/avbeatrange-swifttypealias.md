# AVBeatRange

**Framework**: AVFAudio  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVBeatRange = _AVBeatRange
```

## Topics

### Instance Properties
- [var length: AVMusicTimeStamp](avbeatrange-swift.typealias/length.md)
- [var start: AVMusicTimeStamp](avbeatrange-swift.typealias/start.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](avaudiosequencer/beats(forhosttime:error:).md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](avaudiosequencer/beats(forseconds:).md)
  Gets the beat position (timestamp) for the specified time in the track.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avbeatrange-swift.typealias)*