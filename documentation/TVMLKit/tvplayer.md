# TVPlayer

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.

**Availability**:
- tvOS 12.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVPlayer
```

```objc
@interface TVPlayer : NSObject
```

## Overview

You create a new `TVPlayer` object using your custom [`AVPlayer`](../AVFoundation/avplayer.md) object. You can then play media items that are associated with the JavaScript media player using the new player. For example, you can add gestures, overlays, and other custom features to your TV player.

## Topics

### Setting Up the Player
- [init(player: AVPlayer)](./tvplayer/init%28player%29.md)
  Creates a new customizable player from an existing player.
- [var player: AVPlayer](./tvplayer/player.md)
  The customizable media player.
- [var playlist: TVPlaylist?](./tvplayer/playlist.md)
  The playlist for the media player.
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
- [class TVPlaybackCustomEventUserInfo](./tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.
### Inspecting Media Items
- [func setCurrentMediaItem(toItemAtIndex: Int)](./tvplayer/setcurrentmediaitem%28toitematindex%29.md)
  Sets the current media item to the designated media item.
- [var previousMediaItem: TVMediaItem?](./tvplayer/previousmediaitem.md)
  The previously selected media item.
- [var currentMediaItem: TVMediaItem?](./tvplayer/currentmediaitem.md)
  The currently selected media item.
- [var nextMediaItem: TVMediaItem?](./tvplayer/nextmediaitem.md)
  The next media item in the playlist.
### Instance Methods
- [func present(animated: Bool)](./tvplayer/present%28animated%29.md)

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

## See Also

### Custom Player
- [class TVMediaItem](./tvmediaitem.md)
  A single audio or video item associated with the Apple TV JavaScript player.
- [class TVPlaylist](./tvplaylist.md)
  A collection of media items associated with the Apple TV JavaScript player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer)*