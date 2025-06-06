# AVMusicTimeStamp

**Framework**: AVFAudio  
**Kind**: typealias

A fractional number of beats.

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
typealias AVMusicTimeStamp = Double
```

#### Discussion

Use this value for all sequencer timeline-related methods. The tempo of the sequence determines the relationship between this value and time (in seconds).

## See Also

- [func hostTime(forBeats: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](avaudiosequencer/hosttime(forbeats:error:).md)
  Gets the host time the sequence plays at the specified position.
- [func seconds(forBeats: AVMusicTimeStamp) -> TimeInterval](avaudiosequencer/seconds(forbeats:).md)
  Gets the time for the specified beat position (timestamp) in the track, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictimestamp)*