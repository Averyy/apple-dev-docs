# automaticallyPublishesNowPlayingInfo

**Framework**: Media Player  
**Kind**: property

A Boolean that indicates whether Now Playing info automatically publishes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyPublishesNowPlayingInfo: Bool { get set }
```

#### Discussion

You can set Now Playing information keys for automatic publishing on [`nowPlayingInfo`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem/nowPlayingInfo).

> ❗ **Important**:  If you set `automaticallyPublishesNowPlayingInfo` to `true`, don’t use [`nowPlayingInfoCenter`](mpnowplayingsession/nowplayinginfocenter.md).

## See Also

- [var nowPlayingInfoCenter: MPNowPlayingInfoCenter](mpnowplayingsession/nowplayinginfocenter.md)
  The Now Playing information center associated with the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/automaticallypublishesnowplayinginfo)*