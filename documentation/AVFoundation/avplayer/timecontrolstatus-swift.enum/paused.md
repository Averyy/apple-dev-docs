# AVPlayer.TimeControlStatus.paused

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

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

```c
AVPlayerTimeControlStatusPaused
```

#### Discussion

In this state, the player pauses indefinitely and doesn’t resume playback until you call its play method. You can also resume playback if the player has sufficent data to start playback by calling the player’s [`setRate(_:time:atHostTime:)`](../setrate%28_,time,athosttime%29.md) or [`playImmediately(atRate:)`](../playimmediately%28atrate%29.md) method with a nonzero rate value.

## See Also

### Status values
- [AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate](./waitingtoplayatspecifiedrate.md)
  A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayer.TimeControlStatus.playing](./playing.md)
  A state that indicates that the player is currently playing media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/paused)*