# MPMediaLibraryDidChange

**Framework**: Foundation  
**Kind**: property

Indicates the media library has changed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
static let MPMediaLibraryDidChange: NSNotification.Name
```

#### Discussion

When the system posts this notification, your app should reevaluate items or playlists that you previously cached.

## See Also

- [static let MPMusicPlayerControllerQueueDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollerqueuedidchange.md)
  Indicates the music player’s queue changed.
- [static let MPMediaPlaybackIsPreparedToPlayDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmediaplaybackispreparedtoplaydidchange.md)
  Indicates that the prepared to play status of the media player has changed.
- [static let MPMusicPlayerControllerNowPlayingItemDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollernowplayingitemdidchange.md)
  Posted when the currently playing media item has changed.
- [static let MPMusicPlayerControllerPlaybackStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollerplaybackstatedidchange.md)
  Posted when the playback state changes programmatically or by user action.
- [static let MPMusicPlayerControllerVolumeDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmusicplayercontrollervolumedidchange.md)
  Posted when the audio playback volume for the music player has changed.
- [static let MPMovieDurationAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmoviedurationavailable.md)
  Posted when the duration of a movie has been determined. There is no `userInfo` dictionary.
- [static let MPMovieMediaTypesAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmoviemediatypesavailable.md)
  Posted when the available media types in a movie are determined. There is no `userInfo` dictionary.
- [static let MPMovieNaturalSizeAvailable: NSNotification.Name](nsnotification/name-swift.struct/mpmovienaturalsizeavailable.md)
  Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidEnterFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerdidenterfullscreen.md)
  Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerDidExitFullscreen: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerdidexitfullscreen.md)
  Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary.
- [static let MPMoviePlayerIsAirPlayVideoActiveDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerisairplayvideoactivedidchange.md)
  Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary.
- [static let MPMoviePlayerLoadStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerloadstatedidchange.md)
  Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerNowPlayingMovieDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayernowplayingmoviedidchange.md)
  Posted when the currently playing movie has changed. There is no `userInfo` dictionary.
- [static let MPMoviePlayerPlaybackDidFinish: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerplaybackdidfinish.md)
  Posted when a movie has finished playing.
- [static let MPMoviePlayerPlaybackStateDidChange: NSNotification.Name](nsnotification/name-swift.struct/mpmovieplayerplaybackstatedidchange.md)
  Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mpmedialibrarydidchange)*