# TVPlaybackEventMarshaling

**Framework**: TVMLKit  
**Kind**: protocol  
**Role**: Protocol

A protocol used for sending and receiving information across the JavaScript bridge.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
protocol TVPlaybackEventMarshaling : NSObjectProtocol
```

```objc
@protocol TVPlaybackEventMarshaling <NSObject>
```

## Overview

You must conform to this protocol in order to pass custom events.

## Topics

### Processing Playback Events
- [func processReturnValue(value: JSValue, in: JSContext)](./tvplaybackeventmarshaling/processreturnvalue%28value,in%29.md)
  Converts a JavaScript value into a value that is readable in Swift or Objective-C.
- [var properties: [TVPlaybackEventProperty : Any]?](./tvplaybackeventmarshaling/properties.md)
  An array of custom playback event properties.
- [struct TVPlaybackEventProperty](./tvplaybackeventproperty.md)
  Extend this structure to create your own custom playback event properties.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [TVPlaybackCustomEventUserInfo](./tvplaybackcustomeventuserinfo.md)

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
- [class TVPlaybackCustomEventUserInfo](./tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplaybackeventmarshaling)*