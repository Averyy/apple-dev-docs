# automaticallyWaitsToMinimizeStalling

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.

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
nonisolated
var automaticallyWaitsToMinimizeStalling: Bool { get set }
```

#### Discussion

When playing media delivered over HTTP, this property is used to determine if the player should automatically delay playback in order to minimize stalling. When this property is [`true`](https://developer.apple.com/documentation/swift/true) and the player changes from a paused state ([`rate`](avplayer/rate.md) of `0.0`) to a played state ([`rate`](avplayer/rate.md) > `0.0`), the player will try to determine if the current item can play to its end at the currently specified rate. If it determines that it’s likely to encounter a stall, the value of the player’s [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) will change to [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) and playback will automatically start when the likelihood of stalling has been minimized. A similar condition will occur during playback if the current player item’s playback buffer is exhausted and playback stalls. Playback will automatically resume when the likelihood of stalling has been minimized.

You will need to set this property to [`false`](https://developer.apple.com/documentation/swift/false) when you require precise control over playback start times, such as if you’re are synchronizing multiple player instances using the [`setRate(_:time:atHostTime:)`](avplayer/setrate(_:time:athosttime:).md) method. If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), playback will start immediately when requested as long as the playback buffer is not empty. If the playback buffer becomes empty and playback stalls, the player’s [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) will switch to [`AVPlayer.TimeControlStatus.paused`](avplayer/timecontrolstatus-swift.enum/paused.md) and the playback rate will change to `0.0`.

Changing the value of this property to [`false`](https://developer.apple.com/documentation/swift/false) while the player’s [`timeControlStatus`](avplayer/timecontrolstatus-swift.property.md) is [`AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate`](avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) and its [`reasonForWaitingToPlay`](avplayer/reasonforwaitingtoplay.md) is [`toMinimizeStalls`](avplayer/waitingreason/tominimizestalls.md) will cause the player to immediately attempt playback at the specified rate.

> ❗ **Important**:  For clients linked against iOS 10.0 and later or macOS 10.12 and later (and running on those versions), the default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). This property did not exist in previous OS versions and the observed behavior was dependent on the type of media played: -  When playing HLS media, the player behaved as if [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`true`](https://developer.apple.com/documentation/swift/true).
-  When playing file-based media, including progressively downloaded content, the player behaved as if [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`false`](https://developer.apple.com/documentation/swift/false). You should verify that your playback applications perform as expected using this new default automatic waiting behavior.

 For clients linked against iOS 10.0 and later or macOS 10.12 and later (and running on those versions), the default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). This property did not exist in previous OS versions and the observed behavior was dependent on the type of media played:

-  When playing HLS media, the player behaved as if [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`true`](https://developer.apple.com/documentation/swift/true).
-  When playing file-based media, including progressively downloaded content, the player behaved as if [`automaticallyWaitsToMinimizeStalling`](avplayer/automaticallywaitstominimizestalling.md) is [`false`](https://developer.apple.com/documentation/swift/false).

You should verify that your playback applications perform as expected using this new default automatic waiting behavior.

## See Also

- [var reasonForWaitingToPlay: AVPlayer.WaitingReason?](avplayer/reasonforwaitingtoplay.md)
  The reason the player is currently waiting for playback to begin or resume.
- [AVPlayer.WaitingReason](avplayer/waitingreason.md)
  The reasons a player is waiting to begin or resume playback.
- [var timeControlStatus: AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.property.md)
  A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [AVPlayer.TimeControlStatus](avplayer/timecontrolstatus-swift.enum.md)
  Constants that indicate the state of playback control.
- [func playImmediately(atRate: Float)](avplayer/playimmediately(atrate:).md)
  Plays the available media data immediately, at the specified rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/automaticallywaitstominimizestalling)*