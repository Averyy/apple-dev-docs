# AVBeatRange

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A specific time range within a music track.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVBeatRange = _AVBeatRange
```

## Topics

### Range bounds
- [var start: AVMusicTimeStamp](./avbeatrange-swift.typealias/start.md)
- [var length: AVMusicTimeStamp](./avbeatrange-swift.typealias/length.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Handling beat range
- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forhosttime,error%29.md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forseconds%29.md)
  Gets the beat position (timestamp) for the specified time in the track.
- [var AVMusicTimeStampEndOfTrack: Double](./avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avbeatrange-swift.typealias)*