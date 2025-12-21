# reversePlaybackEndTime

**Framework**: AVFoundation  
**Kind**: property

The time at which reverse playback ends.

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
nonisolated
var reversePlaybackEndTime: CMTime { get set }
```

#### Discussion

The value indicated the time at which playback should end when the playback rate is negative (see `AVPlayer`’s [`rate`](avplayer/rate.md) property).

The default value is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid), which indicates that no end time for reverse playback is specified. In this case, the effective end time for reverse playback is [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero).

The value of this property has no effect on playback when the rate is positive.

## See Also

- [var forwardPlaybackEndTime: CMTime](avplayeritem/forwardplaybackendtime.md)
  The time at which forward playback ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/reverseplaybackendtime)*