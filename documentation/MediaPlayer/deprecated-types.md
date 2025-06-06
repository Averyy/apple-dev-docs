# Deprecated types

**Framework**: Media Player

Review deprecated symbols and avoid using them in your app.

## Topics

### Deprecated symbols
- [class MPMovieAccessLog](mpmovieaccesslog.md)
  Key metrics about network playback for an associated movie player that’s playing streamed content.
- [class MPMovieAccessLogEvent](mpmovieaccesslogevent.md)
  A single piece of information for a movie access log.
- [class MPMovieErrorLog](mpmovieerrorlog.md)
  Data describing network resource playback failures for the associated movie player, including timestamps indicating when each failure occurred.
- [class MPMovieErrorLogEvent](mpmovieerrorlogevent.md)
  A single piece of information for a movie error log.
- [struct MPMovieLoadState](mpmovieloadstate.md)
  Constants describing the network load state of the movie player.
- [struct MPMovieMediaTypeMask](mpmoviemediatypemask.md)
  The types of content available in the movie file.
- [class MPMoviePlayerController](mpmovieplayercontroller.md)
  A type of movie player that manages the playback of a movie from a file or a network stream.
- [class MPMoviePlayerViewController](mpmovieplayerviewcontroller.md)
  A simple view controller for displaying full-screen movies.
- [class MPTimedMetadata](mptimedmetadata.md)
  A  carries time-based information within HTTP streamed media.
- [class MPPlayableContentManager](mpplayablecontentmanager.md)
  A shared content manager for controlling interactions between your media app and system-provided or external media player interfaces.
- [class MPPlayableContentManagerContext](mpplayablecontentmanagercontext.md)
  An object representing the current state of the playable endpoint.
- [class var iPodMusicPlayer: MPMusicPlayerController](mpmusicplayercontroller/ipodmusicplayer.md)
  Returns the iPod music player, which controls the iPod app’s state.
- [convenience init(image: UIImage)](mpmediaitemartwork/init(image:).md)
  Initializes a media item artwork instance with a full-size image.
- [var imageCropRect: CGRect](mpmediaitemartwork/imagecroprect.md)
  The bounds, in points, of the content area for the full size image associated with the media item artwork.
- [var showsRouteButton: Bool](mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](mpvolumeview/routebuttonimage(for:).md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](mpvolumeview/iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [Global volume setting methods](global-volume-setting-methods.md)
  Global functions for setting the volume alert window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/deprecated-types)*