# TVPlaybackEvent

**Framework**: TVMLKit  
**Kind**: struct  
**Role**: Structure

Extend this structure to send your custom playback events to the JavaScript environment.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
struct TVPlaybackEvent
```

```c
typedef NSString * TVPlaybackEvent;
```

## Topics

### Initializers
- [init(String)](./tvplaybackevent/init%28_%29.md)
- [init(rawValue: String)](./tvplaybackevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
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
- [enum TVPlaybackState](./tvplaybackstate.md)
  The possible states of a player.
- [func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?, completion: ((Bool) -> Void)?)](./tvplayer/dispatch%28event,userinfo,completion%29.md)
  Dispatches custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](./tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](./tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackevent)*