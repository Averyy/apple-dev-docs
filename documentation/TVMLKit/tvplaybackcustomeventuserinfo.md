# TVPlaybackCustomEventUserInfo

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

The user information used in a custom playback event.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVPlaybackCustomEventUserInfo
```

```objc
@interface TVPlaybackCustomEventUserInfo : NSObject
```

## Topics

### Creating User Info for Custom Playback Events
- [init(properties: [TVPlaybackEventProperty : Any]?, expectsReturnValue: Bool)](./tvplaybackcustomeventuserinfo/init%28properties,expectsreturnvalue%29.md)
  Create a new custom playback event user info dictionary.
- [struct TVPlaybackEventProperty](./tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.
- [var expectsReturnValue: Bool](./tvplaybackcustomeventuserinfo/expectsreturnvalue.md)
  A Boolean value that indicates whether the custom event expects to contain a return value.
- [var returnValue: Any?](./tvplaybackcustomeventuserinfo/returnvalue.md)
  The return value type for the custom event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [TVPlaybackEventMarshaling](./tvplaybackeventmarshaling.md)

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
- [struct TVPlaybackEvent](./tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [protocol TVPlaybackEventMarshaling](./tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackcustomeventuserinfo)*