# MPMovieSourceTypeAvailableNotification

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Posted when the source type of a movie was previously unknown and is newly available. There is no `userInfo` dictionary.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

## Declaration

```c
extern NSString * const MPMovieSourceTypeAvailableNotification;
```

## Discussion

To retrieve the source type of the movie, access the movie player’s [`movieSourceType`](./mpmovieplayercontroller/moviesourcetype.md) property. The movie player whose state has changed is available as the object associated with the notification.

## See Also

### Notifications
- [MPMoviePlayerDidEnterFullscreenNotification](./mpmovieplayerdidenterfullscreennotification.md)
  Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary.
- [MPMoviePlayerDidExitFullscreenNotification](./mpmovieplayerdidexitfullscreennotification.md)
  Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary.
- [MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification](./mpmovieplayerisairplayvideoactivedidchangenotification.md)
  Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary.
- [MPMoviePlayerLoadStateDidChangeNotification](./mpmovieplayerloadstatedidchangenotification.md)
  Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary.
- [MPMoviePlayerNowPlayingMovieDidChangeNotification](./mpmovieplayernowplayingmoviedidchangenotification.md)
  Posted when the currently playing movie has changed. There is no `userInfo` dictionary.
- [MPMoviePlayerPlaybackDidFinishNotification](./mpmovieplayerplaybackdidfinishnotification.md)
  Posted when a movie has finished playing. The `userInfo` dictionary of this notification contains the [`MPMoviePlayerPlaybackDidFinishReasonUserInfoKey`](./mpmovieplayerplaybackdidfinishreasonuserinfokey.md) key, which indicates the reason that playback finished. This notification is also sent when playback fails because of an error.
- [MPMoviePlayerPlaybackStateDidChangeNotification](./mpmovieplayerplaybackstatedidchangenotification.md)
  Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary.
- [MPMoviePlayerReadyForDisplayDidChangeNotification](./mpmovieplayerreadyfordisplaydidchangenotification.md)
  Posted when the ready for display state changes.
- [MPMoviePlayerScalingModeDidChangeNotification](./mpmovieplayerscalingmodedidchangenotification.md)
  Posted when the scaling mode of a movie player has changed. There is no `userInfo` dictionary.
- [MPMoviePlayerThumbnailImageRequestDidFinishNotification](./mpmovieplayerthumbnailimagerequestdidfinishnotification.md)
  Posted when a request to capture a thumbnail from a movie has finished whether the request succeeded or failed. Upon successful capture of a thumbnail, the `userInfo` dictionary contains values for the following keys:
- [MPMoviePlayerTimedMetadataUpdatedNotification](./mpmovieplayertimedmetadataupdatednotification.md)
  Posted when new timed metadata arrives.
- [MPMoviePlayerWillEnterFullscreenNotification](./mpmovieplayerwillenterfullscreennotification.md)
  Posted when a movie player is about to enter full-screen mode.
- [MPMoviePlayerWillExitFullscreenNotification](./mpmovieplayerwillexitfullscreennotification.md)
  Posted when a movie player is about to exit full-screen mode.
- [MPMovieDurationAvailableNotification](./mpmoviedurationavailablenotification.md)
  Posted when the duration of a movie has been determined. There is no `userInfo` dictionary.
- [MPMovieMediaTypesAvailableNotification](./mpmoviemediatypesavailablenotification.md)
  Posted when the available media types in a movie are determined. There is no `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetypeavailablenotification)*