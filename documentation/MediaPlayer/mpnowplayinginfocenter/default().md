# default()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Returns the singleton Now Playing info center.

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
class func `default`() -> MPNowPlayingInfoCenter
```

```objc
+ (MPNowPlayingInfoCenter *) defaultCenter;
```

#### Return Value

The now playing info center singleton.

#### Discussion

The default now playing info center holds Now Playing information for the app that’s designated to receive remote control events. For information on how to configure your app to receive remote control events, see [Handling external player events notifications](../handling-external-player-events-notifications.md).

## See Also

### Working with the default Now Playing info center
- [var nowPlayingInfo: [String : Any]?](./nowplayinginfo.md)
  The current Now Playing information for the default Now Playing info center.
- [enum MPNowPlayingInfoMediaType](../mpnowplayinginfomediatype.md)
  The type of media currently playing.
- [class var supportedAnimatedArtworkKeys: [String]](./supportedanimatedartworkkeys.md)
  Keys related to animated artwork that are supported by the current platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/default())*