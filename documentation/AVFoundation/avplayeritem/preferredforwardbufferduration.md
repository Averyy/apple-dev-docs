# preferredForwardBufferDuration

**Framework**: AVFoundation  
**Kind**: property

The duration the player should buffer media from the network ahead of the playhead to guard against playback disruption.

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
var preferredForwardBufferDuration: TimeInterval { get set }
```

#### Discussion

This property defines the preferred forward buffer duration in seconds. If set to 0, the player will choose an appropriate level of buffering for most use cases. Setting this property to a low value will increase the chance that playback will stall and re-buffer, while setting it to a high value will increase demand on system resources.

## See Also

- [var preferredPeakBitRate: Double](avplayeritem/preferredpeakbitrate.md)
  The desired limit, in bits per second, of network bandwidth consumption for this item.
- [var canUseNetworkResourcesForLiveStreamingWhilePaused: Bool](avplayeritem/canusenetworkresourcesforlivestreamingwhilepaused.md)
  A Boolean value that indicates whether the player item can use network resources to keep the playback state up to date while paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredforwardbufferduration)*