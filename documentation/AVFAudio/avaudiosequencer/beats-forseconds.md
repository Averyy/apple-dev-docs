# beats(forSeconds:)

**Framework**: AVFAudio  
**Kind**: method

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

## Parameters

- `seconds`: The time to retrieve the beat timestamp for.

## See Also

- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](avaudiosequencer/beats(forhosttime:error:).md)
  Gets the beat the system plays at the specified host time.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/beats(forseconds:))*