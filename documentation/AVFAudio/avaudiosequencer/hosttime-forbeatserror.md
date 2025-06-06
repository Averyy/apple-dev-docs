# hostTime(forBeats:error:)

**Framework**: AVFAudio  
**Kind**: method

Gets the host time the sequence plays at the specified position.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func hostTime(forBeats inBeats: AVMusicTimeStamp, error outError: NSErrorPointer) -> UInt64
```

#### Discussion

This call is valid when the player is in a playing state. It returns `0` with an error, otherwise, or if the starting position of the player is after the specified beat. The method uses the sequence’s tempo map to translate a beat time from the starting time and the beat of the player.

## Parameters

- `inBeats`: The timestamp for the beat position.
- `outError`: On exit, if an error occurs, a description of the error.

## See Also

- [typealias AVMusicTimeStamp](avmusictimestamp.md)
  A fractional number of beats.
- [func seconds(forBeats: AVMusicTimeStamp) -> TimeInterval](avaudiosequencer/seconds(forbeats:).md)
  Gets the time for the specified beat position (timestamp) in the track, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/hosttime(forbeats:error:))*