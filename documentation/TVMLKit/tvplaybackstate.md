# TVPlaybackState

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The possible states of a player.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVPlaybackState
```

```c
enum TVPlaybackState : NSInteger;
```

## Topics

### Playback States
- [TVPlaybackState.undefined](./tvplaybackstate/undefined.md)
  The playback state of the player is undefined.
- [TVPlaybackState.begin](./tvplaybackstate/begin.md)
  The player is beginning playback.
- [TVPlaybackState.loading](./tvplaybackstate/loading.md)
  The player is loading a media item.
- [TVPlaybackState.playing](./tvplaybackstate/playing.md)
  The player is currently playing.
- [TVPlaybackState.paused](./tvplaybackstate/paused.md)
  The player paused playback.
- [TVPlaybackState.scanning](./tvplaybackstate/scanning.md)
  The player is quickly scanning forwards or backwards.
- [TVPlaybackState.fastForwarding](./tvplaybackstate/fastforwarding.md)
  The player is fast-forwarding.
- [TVPlaybackState.rewinding](./tvplaybackstate/rewinding.md)
  The player is rewinding.
- [TVPlaybackState.end](./tvplaybackstate/end.md)
  The player ended playback.
### Initializers
- [init?(rawValue: Int)](./tvplaybackstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling Playback
- [func next()](./tvplayer/next%28%29.md)
  Plays the next media item in the playlist.
- [func pause()](./tvplayer/pause%28%29.md)
  Pauses the currently playing item.
- [func previous()](./tvplayer/previous%28%29.md)
  Plays the previous media item in the playlist.
- [var state: TVPlaybackState](./tvplayer/state.md)
  The current state of the player.
- [func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?, completion: ((Bool) -> Void)?)](./tvplayer/dispatch%28event,userinfo,completion%29.md)
  Dispatches custom playback events to the JavaScript environment.
- [struct TVPlaybackEvent](./tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](./tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](./tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackstate)*