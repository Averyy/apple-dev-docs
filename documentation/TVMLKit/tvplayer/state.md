# state

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The current state of the player.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var state: TVPlaybackState { get }
```

```objc
@property (nonatomic, assign, readonly) TVPlaybackState state;
```

## See Also

### Controlling Playback
- [func next()](./next%28%29.md)
  Plays the next media item in the playlist.
- [func pause()](./pause%28%29.md)
  Pauses the currently playing item.
- [func previous()](./previous%28%29.md)
  Plays the previous media item in the playlist.
- [enum TVPlaybackState](../tvplaybackstate.md)
  The possible states of a player.
- [func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?, completion: ((Bool) -> Void)?)](./dispatch%28event,userinfo,completion%29.md)
  Dispatches custom playback events to the JavaScript environment.
- [struct TVPlaybackEvent](../tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](../tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](../tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/state)*