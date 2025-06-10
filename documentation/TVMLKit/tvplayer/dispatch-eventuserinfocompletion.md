# dispatch(event:userInfo:completion:)

**Framework**: TVMLKit  
**Kind**: method

Dispatches custom playback events to the JavaScript environment.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `event`: The custom playback event to be dispatched.
- `userInfo`: The user information for the custom event.
- `completion`: A block that is called after the event has been dispatched. Contains the information required to process the event’s results.

## See Also

- [func next()](tvplayer/next.md)
  Plays the next media item in the playlist.
- [func pause()](tvplayer/pause.md)
  Pauses the currently playing item.
- [func previous()](tvplayer/previous.md)
  Plays the previous media item in the playlist.
- [var state: TVPlaybackState](tvplayer/state.md)
  The current state of the player.
- [enum TVPlaybackState](tvplaybackstate.md)
  The possible states of a player.
- [struct TVPlaybackEvent](tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer/dispatch(event:userinfo:completion:))*