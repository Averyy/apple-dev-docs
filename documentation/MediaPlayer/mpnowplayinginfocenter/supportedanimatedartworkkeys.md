# supportedAnimatedArtworkKeys

**Framework**: Media Player  
**Kind**: property

Keys related to animated artwork that are supported by the current platform.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class var supportedAnimatedArtworkKeys: [String] { get }
```

## Mentions

- [Providing animated artwork for media items](providing-animated-artwork-for-media-items.md)

#### Discussion

If you specify an instance of animated artwork (an `MPMediaItemAnimatedArtwork`) to `nowPlayingInfo` using any key not in this collection it will be ignored.

## See Also

- [class func `default`() -> MPNowPlayingInfoCenter](mpnowplayinginfocenter/default.md)
  Returns the singleton Now Playing info center.
- [var nowPlayingInfo: [String : Any]?](mpnowplayinginfocenter/nowplayinginfo.md)
  The current Now Playing information for the default Now Playing info center.
- [enum MPNowPlayingInfoMediaType](mpnowplayinginfomediatype.md)
  The type of media currently playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/supportedanimatedartworkkeys)*