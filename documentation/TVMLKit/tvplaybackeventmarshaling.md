# TVPlaybackEventMarshaling

**Framework**: TVMLKit  
**Kind**: protocol

A protocol used for sending and receiving information across the JavaScript bridge.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
protocol TVPlaybackEventMarshaling : NSObjectProtocol
```

#### Overview

You must conform to this protocol in order to pass custom events.

## Topics

### Processing Playback Events
- [func processReturnValue(value: JSValue, in: JSContext)](tvplaybackeventmarshaling/processreturnvalue(value:in:).md)
  Converts a JavaScript value into a value that is readable in Swift or Objective-C.
- [var properties: [TVPlaybackEventProperty : Any]?](tvplaybackeventmarshaling/properties.md)
  An array of custom playback event properties.
- [struct TVPlaybackEventProperty](tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [TVPlaybackCustomEventUserInfo](tvplaybackcustomeventuserinfo.md)

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
- [func dispatch(event: TVPlaybackEvent, userInfo: (any TVPlaybackEventMarshaling)?, completion: ((Bool) -> Void)?)](tvplayer/dispatch(event:userinfo:completion:).md)
  Dispatches custom playback events to the JavaScript environment.
- [struct TVPlaybackEvent](tvplaybackevent.md)
  Extend this structure to send your custom playback events to the JavaScript environment.
- [class TVPlaybackCustomEventUserInfo](tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventmarshaling)*