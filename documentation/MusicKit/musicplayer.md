# MusicPlayer

**Framework**: MusicKit  
**Kind**: class

An object your app uses to play music.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MusicPlayer
```

## Topics

### Classes
- [MusicPlayer.Queue](musicplayer/queue.md)
  A representation of the playback queue for a music player.
- [MusicPlayer.State](musicplayer/state-swift.class.md)
  An object that exposes the observable properties of a music player.
### Instance Properties
- [var isPreparedToPlay: Bool](musicplayer/ispreparedtoplay.md)
  A Boolean value that indicates whether a music player is ready to play.
- [var playbackTime: TimeInterval](musicplayer/playbacktime.md)
  The current playback time, in seconds, of the current entry.
- [let state: MusicPlayer.State](musicplayer/state-swift.property.md)
  An object that exposes the observable properties of the music player.
### Instance Methods
- [func beginSeekingBackward()](musicplayer/beginseekingbackward.md)
  Begins seeking backward through the music content.
- [func beginSeekingForward()](musicplayer/beginseekingforward.md)
  Begins seeking forward through the music content.
- [func endSeeking()](musicplayer/endseeking.md)
  Ends forward and backward seeking through the music content.
- [func pause()](musicplayer/pause.md)
  Pauses playback of the current entry.
- [func play() async throws](musicplayer/play.md)
  Initiates playback from the current queue.
- [func prepareToPlay() async throws](musicplayer/preparetoplay.md)
  Prepares the current queue for playback, interrupting any active (nonmixable) audio sessions.
- [func restartCurrentEntry()](musicplayer/restartcurrententry.md)
  Restarts playback at the beginning of the currently playing entry.
- [func skipToNextEntry() async throws](musicplayer/skiptonextentry.md)
  Starts playback of the next entry in the playback queue.
- [func skipToPreviousEntry() async throws](musicplayer/skiptopreviousentry.md)
  Starts playback of the previous entry in the playback queue.
- [func stop()](musicplayer/stop.md)
  Ends playback of the current entry.
### Enumerations
- [MusicPlayer.PlaybackStatus](musicplayer/playbackstatus.md)
  The music player playback status modes.
- [MusicPlayer.RepeatMode](musicplayer/repeatmode.md)
  The repeat modes for the music player.
- [MusicPlayer.ShuffleMode](musicplayer/shufflemode.md)
  The shuffle modes for the music player.
- [MusicPlayer.Transition](musicplayer/transition.md)
  The transition applied between playing items.

## Relationships

### Inherited By
- [ApplicationMusicPlayer](applicationmusicplayer.md)
- [SystemMusicPlayer](systemmusicplayer.md)

## See Also

- [class ApplicationMusicPlayer](applicationmusicplayer.md)
  An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [class SystemMusicPlayer](systemmusicplayer.md)
  An object your app uses to play music by controlling the Music app’s state.
- [protocol PlayableMusicItem](playablemusicitem.md)
  A set of properties that a music player uses to initiate playback for a music item.
- [struct PlayParameters](playparameters.md)
  An opaque object that represents parameters to initiate playback of a playable music item using a music player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer)*