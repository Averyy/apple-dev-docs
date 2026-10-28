# AVMusicTimeStamp

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A fractional number of beats.

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
typealias AVMusicTimeStamp = Double
```

```c
typedef double AVMusicTimeStamp;
```

## Discussion

Use this value for all sequencer timeline-related methods. The tempo of the sequence determines the relationship between this value and time (in seconds).

## See Also

### Managing time stamps
- [func hostTime(forBeats: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](./avaudiosequencer/hosttime%28forbeats,error%29.md)
  Gets the host time the sequence plays at the specified position.
- [func seconds(forBeats: AVMusicTimeStamp) -> TimeInterval](./avaudiosequencer/seconds%28forbeats%29.md)
  Gets the time for the specified beat position (timestamp) in the track, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictimestamp)*