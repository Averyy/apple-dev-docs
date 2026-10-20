# seconds(forBeats:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Gets the time for the specified beat position (timestamp) in the track, in seconds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func seconds(forBeats beats: AVMusicTimeStamp) -> TimeInterval
```

```objc
- (NSTimeInterval) secondsForBeats:(AVMusicTimeStamp) beats;
```

## Parameters

- `beats`: The timestamp for the beat position.

## See Also

### Managing time stamps
- [typealias AVMusicTimeStamp](../avmusictimestamp.md)
  A fractional number of beats.
- [func hostTime(forBeats: AVMusicTimeStamp, error: NSErrorPointer) -> UInt64](./hosttime%28forbeats,error%29.md)
  Gets the host time the sequence plays at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/seconds(forbeats:))*