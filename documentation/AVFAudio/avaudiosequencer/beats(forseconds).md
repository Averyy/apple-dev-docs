# beats(forSeconds:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Gets the beat position (timestamp) for the specified time in the track.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func beats(forSeconds seconds: TimeInterval) -> AVMusicTimeStamp
```

```objc
- (AVMusicTimeStamp) beatsForSeconds:(NSTimeInterval) seconds;
```

## Parameters

- `seconds`: The time to retrieve the beat timestamp for.

## See Also

### Handling beat range
- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](./beats%28forhosttime,error%29.md)
  Gets the beat the system plays at the specified host time.
- [var AVMusicTimeStampEndOfTrack: Double](../avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.
- [typealias AVBeatRange](../avbeatrange-swift.typealias.md)
  A specific time range within a music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/beats(forseconds:))*