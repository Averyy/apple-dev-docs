# next()

**Framework**: TVMLKit  
**Kind**: method

Plays the next media item in the playlist.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
func next()
```

## See Also

- [func pause()](tvplayer/pause.md)
  Pauses the currently playing item.
- [func previous()](tvplayer/previous.md)
  Plays the previous media item in the playlist.
- [var state: TVPlaybackState](tvplayer/state.md)
  The current state of the player.
- [enum TVPlaybackState](tvplaybackstate.md)
  The possible states of a player.
- [func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?, completion: ((Bool) -> Void)?)](tvplayer/dispatch(event:userinfo:completion:).md)
  Dispatches custom playback events to the JavaScript environment.
- [struct TVPlaybackEvent](tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/next())*