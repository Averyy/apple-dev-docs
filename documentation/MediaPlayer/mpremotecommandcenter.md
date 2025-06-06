# MPRemoteCommandCenter

**Framework**: Media Player  
**Kind**: class

An object that responds to remote control events sent by external accessories and system controls.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPRemoteCommandCenter
```

## Mentions

- [Handling external player events notifications](handling-external-player-events-notifications.md)

#### Overview

Don’t create instances of this class yourself. Instead, use the [`shared()`](mpremotecommandcenter/shared().md) method to retrieve the shared command center object. The properties of the shared command center object contain [`MPRemoteCommand`](mpremotecommand.md) objects that respond to the various kinds of remote control events. You configure these objects to respond to the events you’re interested to handle in your app.

## Topics

### Retrieving the shared instance
- [class func shared() -> MPRemoteCommandCenter](mpremotecommandcenter/shared.md)
  Returns the shared object you use to access the system’s remote command objects.
### Playback commands
- [var pauseCommand: MPRemoteCommand](mpremotecommandcenter/pausecommand.md)
  The command object for pausing playback of the current item.
- [var playCommand: MPRemoteCommand](mpremotecommandcenter/playcommand.md)
  The command object for starting playback of the current item.
- [var stopCommand: MPRemoteCommand](mpremotecommandcenter/stopcommand.md)
  The command object for stopping playback of the current item.
- [var togglePlayPauseCommand: MPRemoteCommand](mpremotecommandcenter/toggleplaypausecommand.md)
  The command object for toggling between playing and pausing the current item.
### Navigating between tracks
- [var nextTrackCommand: MPRemoteCommand](mpremotecommandcenter/nexttrackcommand.md)
  The command object for selecting the next track.
- [var previousTrackCommand: MPRemoteCommand](mpremotecommandcenter/previoustrackcommand.md)
  The command object for selecting the previous track.
- [var changeRepeatModeCommand: MPChangeRepeatModeCommand](mpremotecommandcenter/changerepeatmodecommand.md)
  The command object for changing the repeat mode.
- [var changeShuffleModeCommand: MPChangeShuffleModeCommand](mpremotecommandcenter/changeshufflemodecommand.md)
  The command object for changing the shuffle mode.
### Navigating a track’s contents
- [var changePlaybackRateCommand: MPChangePlaybackRateCommand](mpremotecommandcenter/changeplaybackratecommand.md)
  The command object for changing the playback rate of the current media item.
- [var seekBackwardCommand: MPRemoteCommand](mpremotecommandcenter/seekbackwardcommand.md)
  The command object for seeking backward through a single media item.
- [var seekForwardCommand: MPRemoteCommand](mpremotecommandcenter/seekforwardcommand.md)
  The command object for seeking forward through a single media item.
- [var skipBackwardCommand: MPSkipIntervalCommand](mpremotecommandcenter/skipbackwardcommand.md)
  The command object for playing a previous point in a media item.
- [var skipForwardCommand: MPSkipIntervalCommand](mpremotecommandcenter/skipforwardcommand.md)
  The command object for playing a future point in a media item.
- [var changePlaybackPositionCommand: MPChangePlaybackPositionCommand](mpremotecommandcenter/changeplaybackpositioncommand.md)
  The command object for changing the playback position in a media item.
### Rating a media item
- [var ratingCommand: MPRatingCommand](mpremotecommandcenter/ratingcommand.md)
  The command object for rating a media item.
- [var likeCommand: MPFeedbackCommand](mpremotecommandcenter/likecommand.md)
  The command object for indicating that a user likes what is currently playing.
- [var dislikeCommand: MPFeedbackCommand](mpremotecommandcenter/dislikecommand.md)
  The command object for indicating that a user dislikes what is currently playing.
### Bookmarking a media item
- [var bookmarkCommand: MPFeedbackCommand](mpremotecommandcenter/bookmarkcommand.md)
  The command object for indicating that a user wants to remember a media item.
### Enabling language options
- [var enableLanguageOptionCommand: MPRemoteCommand](mpremotecommandcenter/enablelanguageoptioncommand.md)
  The command object for enabling a language option.
- [var disableLanguageOptionCommand: MPRemoteCommand](mpremotecommandcenter/disablelanguageoptioncommand.md)
  The command object for disabling a language option

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

- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPRemoteCommand](mpremotecommand.md)
  An object that responds to remote command events.
- [class MPRemoteCommandEvent](mpremotecommandevent.md)
  A description of a command sent by an external media player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)*