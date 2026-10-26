# MPMediaPlayback

**Framework**: Media Player  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the interface for controlling audio media playback.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPMediaPlayback
```

```objc
@protocol MPMediaPlayback
```

## Mentions

- [Playing audio using the built-in music player](./playing-audio-using-the-built-in-music-player.md)

#### Overview

This protocol supports basic transport operations including start, stop, and pause, and also lets you seek forward and back through media or to a specific point in its timeline.

## Topics

### Starting and stopping playback
- [func play()](./mpmediaplayback/play%28%29.md)
  Initiates playback of the current item.
- [func pause()](./mpmediaplayback/pause%28%29.md)
  Pauses playback of the current item.
- [func stop()](./mpmediaplayback/stop%28%29.md)
  Ends playback of the current item.
- [func prepareToPlay()](./mpmediaplayback/preparetoplay%28%29.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](./mpmediaplayback/ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.
### Seeking within media
- [func beginSeekingBackward()](./mpmediaplayback/beginseekingbackward%28%29.md)
  Begins seeking backward through the media content.
- [func beginSeekingForward()](./mpmediaplayback/beginseekingforward%28%29.md)
  Begins seeking forward through the media content.
- [func endSeeking()](./mpmediaplayback/endseeking%28%29.md)
  Ends forward and backward seeking through the media content.
### Accessing playback attributes
- [var currentPlaybackRate: Float](./mpmediaplayback/currentplaybackrate.md)
  The current playback rate for the player.
- [var currentPlaybackTime: TimeInterval](./mpmediaplayback/currentplaybacktime.md)
  The current position of the playhead.
### Notifications
- [MPMediaPlaybackIsPreparedToPlayDidChangeNotification](./mpmediaplaybackispreparedtoplaydidchangenotification.md)
  Indicates that the prepared to play status of the media player has changed.

## Relationships

### Conforming Types
- [MPMoviePlayerController](./mpmovieplayercontroller.md)
- [MPMusicPlayerApplicationController](./mpmusicplayerapplicationcontroller.md)
- [MPMusicPlayerController](./mpmusicplayercontroller.md)

## See Also

### Built-in music playback
- [Playing audio using the built-in music player](./playing-audio-using-the-built-in-music-player.md)
  Create a media player inside your app to play audio from the user’s media library.
- [class MPMusicPlayerController](./mpmusicplayercontroller.md)
  An object that plays audio media items from the device’s Music app library.
- [protocol MPSystemMusicPlayerController](./mpsystemmusicplayercontroller.md)
  A protocol for playing videos in the Music app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback)*