# AVMusicTimeStampEndOfTrack

**Framework**: AVFAudio  
**Kind**: var

A timestamp you use to access all events in a music track through a beat range.

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
var AVMusicTimeStampEndOfTrack: Double { get }
```

#### Discussion

Pass this value as the length of an `AVBeatRange` to indicate an end time beyond the last event in the track. This makes it possible to specify a beat range that includes all events starting at a particular time, up to and including the last event.

## See Also

- [func beats(forHostTime: UInt64, error: NSErrorPointer) -> AVMusicTimeStamp](avaudiosequencer/beats(forhosttime:error:).md)
  Gets the beat the system plays at the specified host time.
- [func beats(forSeconds: TimeInterval) -> AVMusicTimeStamp](avaudiosequencer/beats(forseconds:).md)
  Gets the beat position (timestamp) for the specified time in the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictimestampendoftrack)*