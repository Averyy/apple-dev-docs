# beats(forHostTime:error:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Gets the beat the system plays at the specified host time.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func beats(forHostTime inHostTime: UInt64, error outError: NSErrorPointer) -> AVMusicTimeStamp
```

```objc
- (AVMusicTimeStamp) beatsForHostTime:(UInt64) inHostTime error:(NSError **) outError;
```

#### Discussion

This call is valid when the player is in a playing state. It returns `0` with an error, otherwise, or if the starting position of the player is after the specified host time. This method uses the sequence’s tempo map to retrieve a beat time from the specified host time.

## Parameters

- `inHostTime`: The host time for the beat position.
- `outError`: On exit, if an error occurs, a description of the error.

## See Also

### Handling beat range
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](./beats%28forseconds%29.md)
  Gets the beat position (timestamp) for the specified time in the track.
- [var AVMusicTimeStampEndOfTrack: Double](../avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.
- [typealias AVBeatRange](../avbeatrange-swift.typealias.md)
  A specific time range within a music track.
- [AVBeatRange](../avbeatrange-c.struct.md)
  A specific time range within a music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/beats(forhosttime:error:))*