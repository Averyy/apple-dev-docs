# AVMusicTimeStampEndOfTrack

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A timestamp you use to access all events in a music track through a beat range.

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
var AVMusicTimeStampEndOfTrack: Double { get }
```

```c
#define AVMusicTimeStampEndOfTrack
```

## Discussion

Pass this value as the length of an [`AVBeatRange`](./avbeatrange-c.struct.md) to indicate an end time beyond the last event in the track. This makes it possible to specify a beat range that includes all events starting at a particular time, up to and including the last event.

## See Also

### Handling beat range
- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forhosttime,error%29.md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](./avaudiosequencer/beats%28forseconds%29.md)
  Gets the beat position (timestamp) for the specified time in the track.
- [typealias AVBeatRange](./avbeatrange-swift.typealias.md)
  A specific time range within a music track.
- [AVBeatRange](./avbeatrange-c.struct.md)
  A specific time range within a music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictimestampendoftrack)*