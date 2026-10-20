# forwardPlaybackEndTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time at which forward playback ends.

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
nonisolated
var forwardPlaybackEndTime: CMTime { get set }
```

```objc
@property CMTime forwardPlaybackEndTime;
```

#### Discussion

The value indicates the time at which playback should end when the playback rate is positive (see `AVPlayer`’s [`rate`](../avplayer/rate.md) property).

The default value is [`invalid`](../../CoreMedia/cmtime/invalid.md), which indicates that no end time for forward playback is specified. In this case, the effective end time for forward playback is the item’s duration.

The value of this property has no effect on playback when the rate is negative.

## See Also

### Setting playback boundaries
- [var reversePlaybackEndTime: CMTime](./reverseplaybackendtime.md)
  The time at which reverse playback ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/forwardplaybackendtime)*