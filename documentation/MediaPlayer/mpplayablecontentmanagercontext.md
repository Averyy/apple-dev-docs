# MPPlayableContentManagerContext

**Framework**: Media Player  
**Kind**: class

An object representing the current state of the playable endpoint.

**Availability**:
- iOS 8.4+
- iPadOS 8.4+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPPlayableContentManagerContext
```

## Topics

### Inspecting content manager properties
- [var contentLimitsEnforced: Bool](mpplayablecontentmanagercontext/contentlimitsenforced.md)
  A Boolean value that indicates whether the content server enforces content limits.
- [var endpointAvailable: Bool](mpplayablecontentmanagercontext/endpointavailable.md)
  Returns a Boolean that indicates whether the content server is available.
- [var enforcedContentItemsCount: Int](mpplayablecontentmanagercontext/enforcedcontentitemscount.md)
  Returns the number of content items to display during content limiting.
- [var enforcedContentTreeDepth: Int](mpplayablecontentmanagercontext/enforcedcontenttreedepth.md)
  The maximum depth of the navigation hierarchy allowed by the content server.
- [var contentLimitsEnabled: Bool](mpplayablecontentmanagercontext/contentlimitsenabled.md)
  A Boolean value that indicates whether the content server enables content limits.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext)*