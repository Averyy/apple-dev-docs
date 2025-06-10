# supportedAnimatedArtworkKeys

**Framework**: Media Player  
**Kind**: property

Keys related to animated artwork that are supported by the current platform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class var supportedAnimatedArtworkKeys: [String] { get }
```

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