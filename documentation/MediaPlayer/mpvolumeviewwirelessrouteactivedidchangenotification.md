# MPVolumeViewWirelessRouteActiveDidChangeNotification

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Indicates the active wireless route changed.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

## Declaration

```c
extern NSString * const MPVolumeViewWirelessRouteActiveDidChangeNotification;
```

## Discussion

The system posts this notification when the [`isWirelessRouteActive`](./mpvolumeview/iswirelessrouteactive.md) property changes.

## See Also

### Deprecated symbols
- [class MPMovieAccessLog](./mpmovieaccesslog.md)
  Key metrics about network playback for an associated movie player that’s playing streamed content.
- [class MPMovieAccessLogEvent](./mpmovieaccesslogevent.md)
  A single piece of information for a movie access log.
- [class MPMovieErrorLog](./mpmovieerrorlog.md)
  Data describing network resource playback failures for the associated movie player, including timestamps indicating when each failure occurred.
- [class MPMovieErrorLogEvent](./mpmovieerrorlogevent.md)
  A single piece of information for a movie error log.
- [struct MPMovieLoadState](./mpmovieloadstate.md)
  Constants describing the network load state of the movie player.
- [struct MPMovieMediaTypeMask](./mpmoviemediatypemask.md)
  The types of content available in the movie file.
- [class MPMoviePlayerController](./mpmovieplayercontroller.md)
  A type of movie player that manages the playback of a movie from a file or a network stream.
- [class MPMoviePlayerViewController](./mpmovieplayerviewcontroller.md)
  A simple view controller for displaying full-screen movies.
- [class MPTimedMetadata](./mptimedmetadata.md)
  A *timed metadata object that* carries time-based information within HTTP streamed media.
- [class MPPlayableContentManager](./mpplayablecontentmanager.md)
  A shared content manager for controlling interactions between your media app and system-provided or external media player interfaces.
- [class MPPlayableContentManagerContext](./mpplayablecontentmanagercontext.md)
  An object representing the current state of the playable endpoint.
- [class var iPodMusicPlayer: MPMusicPlayerController](./mpmusicplayercontroller/ipodmusicplayer.md)
  Returns the iPod music player, which controls the iPod app’s state.
- [convenience init(image: UIImage)](./mpmediaitemartwork/init%28image%29.md)
  Initializes a media item artwork instance with a full-size image.
- [var imageCropRect: CGRect](./mpmediaitemartwork/imagecroprect.md)
  The bounds, in points, of the content area for the full size image associated with the media item artwork.
- [var showsRouteButton: Bool](./mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeviewwirelessrouteactivedidchangenotification)*