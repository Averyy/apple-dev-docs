# MPNowPlayingInfoMediaType

**Framework**: Media Player  
**Kind**: enum

The type of media currently playing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MPNowPlayingInfoMediaType
```

## Topics

### Enumeration Cases
- [MPNowPlayingInfoMediaType.none](mpnowplayinginfomediatype/none.md)
  There is no now playing media item.
- [MPNowPlayingInfoMediaType.audio](mpnowplayinginfomediatype/audio.md)
  The now playing media item is an audio item.
- [MPNowPlayingInfoMediaType.none](mpnowplayinginfomediatype/none.md)
  There is no now playing media item.
- [MPNowPlayingInfoMediaType.video](mpnowplayinginfomediatype/video.md)
  The now playing media item is a video item.
### Initializers
- [init?(rawValue: UInt)](mpnowplayinginfomediatype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func `default`() -> MPNowPlayingInfoCenter](mpnowplayinginfocenter/default.md)
  Returns the singleton Now Playing info center.
- [var nowPlayingInfo: [String : Any]?](mpnowplayinginfocenter/nowplayinginfo.md)
  The current Now Playing information for the default Now Playing info center.
- [class var supportedAnimatedArtworkKeys: [String]](mpnowplayinginfocenter/supportedanimatedartworkkeys.md)
  Keys related to animated artwork that are supported by the current platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype)*