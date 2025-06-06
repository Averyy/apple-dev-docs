# TVPlayer

**Framework**: TVMLKit  
**Kind**: class

A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVPlayer
```

#### Overview

You create a new `TVPlayer` object using your custom [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object. You can then play media items that are associated with the JavaScript media player using the new player. For example, you can add gestures, overlays, and other custom features to your TV player.

## Topics

### Setting Up the Player
- [init(player: AVPlayer)](tvplayer/init(player:).md)
  Creates a new customizable player from an existing player.
- [var player: AVPlayer](tvplayer/player.md)
  The customizable media player.
- [var playlist: TVPlaylist?](tvplayer/playlist.md)
  The playlist for the media player.
### Controlling Playback
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
- [protocol TVPlaybackEventMarshaling](tvplaybackeventmarshaling.md)
  A protocol used for sending and receiving information across the JavaScript bridge.
- [class TVPlaybackCustomEventUserInfo](tvplaybackcustomeventuserinfo.md)
  The user information used in a custom playback event.
### Inspecting Media Items
- [func setCurrentMediaItem(toItemAtIndex: Int)](tvplayer/setcurrentmediaitem(toitematindex:).md)
  Sets the current media item to the designated media item.
- [var previousMediaItem: TVMediaItem?](tvplayer/previousmediaitem.md)
  The previously selected media item.
- [var currentMediaItem: TVMediaItem?](tvplayer/currentmediaitem.md)
  The currently selected media item.
- [var nextMediaItem: TVMediaItem?](tvplayer/nextmediaitem.md)
  The next media item in the playlist.
### Instance Methods
- [func present(animated: Bool)](tvplayer/present(animated:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVMediaItem](tvmediaitem.md)
  A single audio or video item associated with the Apple TV JavaScript player.
- [class TVPlaylist](tvplaylist.md)
  A collection of media items associated with the Apple TV JavaScript player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvplayer)*