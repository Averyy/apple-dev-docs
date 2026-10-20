# previous()

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Plays the previous media item in the playlist.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func previous()
```

```objc
- (void) previous;
```

## See Also

### Controlling Playback
- [func next()](./next%28%29.md)
  Plays the next media item in the playlist.
- [func pause()](./pause%28%29.md)
  Pauses the currently playing item.
- [var state: TVPlaybackState](./state.md)
  The current state of the player.
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

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/previous())*