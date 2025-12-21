# nowPlayingInfo

**Framework**: Media Player  
**Kind**: property

The current Now Playing information for the default Now Playing info center.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var nowPlayingInfo: [String : Any]? { get set }
```

## Mentions

- [Providing animated artwork for media items](providing-animated-artwork-for-media-items.md)

#### Discussion

To clear the now playing info center dictionary, set it to `nil`.

## See Also

- [class func `default`() -> MPNowPlayingInfoCenter](mpnowplayinginfocenter/default.md)
  Returns the singleton Now Playing info center.
- [enum MPNowPlayingInfoMediaType](mpnowplayinginfomediatype.md)
  The type of media currently playing.
- [class var supportedAnimatedArtworkKeys: [String]](mpnowplayinginfocenter/supportedanimatedartworkkeys.md)
  Keys related to animated artwork that are supported by the current platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/nowplayinginfo)*