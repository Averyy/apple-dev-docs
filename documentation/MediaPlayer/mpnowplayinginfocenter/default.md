# default()

**Framework**: Media Player  
**Kind**: method

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

#### Return Value

The now playing info center singleton.

#### Discussion

The default now playing info center holds Now Playing information for the app that’s designated to receive remote control events. For information on how to configure your app to receive remote control events, see [`Handling external player events notifications`](handling-external-player-events-notifications.md).

## See Also

- [var nowPlayingInfo: [String : Any]?](mpnowplayinginfocenter/nowplayinginfo.md)
  The current Now Playing information for the default Now Playing info center.
- [enum MPNowPlayingInfoMediaType](mpnowplayinginfomediatype.md)
  The type of media currently playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/default())*