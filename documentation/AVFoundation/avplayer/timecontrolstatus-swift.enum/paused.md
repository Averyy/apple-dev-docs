# AVPlayer.TimeControlStatus.paused

**Framework**: AVFoundation  
**Kind**: case

A state that indicates the player paused playback indefinitely.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case paused
```

#### Discussion

In this state, the player pauses indefinitely and doesn’t resume playback until you call its play method. You can also resume playback if the player has sufficent data to start playback by calling the player’s [`setRate(_:time:atHostTime:)`](avplayer/setrate(_:time:athosttime:).md) or [`playImmediately(atRate:)`](avplayer/playimmediately(atrate:).md) method with a nonzero rate value.

## See Also

- [AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md)
  A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayer.TimeControlStatus.playing](avplayer/timecontrolstatus-swift.enum/playing.md)
  A state that indicates that the player is currently playing media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/paused)*