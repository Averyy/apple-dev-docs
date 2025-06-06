# MPTimedMetadata

**Framework**: Media Player  
**Kind**: class

A  carries time-based information within HTTP streamed media.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MPTimedMetadata
```

#### Overview

Content providers can embed these objects when creating a stream. The properties and constants in this class let you extract the metadata as you play the stream using an [`MPMoviePlayerController`](mpmovieplayercontroller.md) object. For example, the provider of a live sports video stream could use `MPTimedMetadata` instances to embed game scores, with timestamps, in the stream. On the client side—that is, on the user’s device—their application could employ the properties of this class to update their app’s user interface in real time during the game.

A Javascript implementation of this class is also available for use by web-based applications.

## Topics

### Extracting timed metadata from a stream
- [var allMetadata: [AnyHashable : Any]!](mptimedmetadata/allmetadata.md)
  A dictionary containing all the metadata in the object.
- [var key: String!](mptimedmetadata/key.md)
  A key that identifies a piece of timed metadata.
- [var keyspace: String!](mptimedmetadata/keyspace.md)
  The namespace of the identifying key.
- [var timestamp: TimeInterval](mptimedmetadata/timestamp.md)
  The timestamp of the metadata, in the timebase of the media stream.
- [var value: Any!](mptimedmetadata/value.md)
  The timed metadata.
### Constants
- [Timed metadata dictionary keys](timed-metadata-dictionary-keys.md)
  Dictionary keys for use with the [`allMetadata`](mptimedmetadata/allmetadata.md) property. All keys are optional.
### Notifications
- [let MPMoviePlayerTimedMetadataUserInfoKey: String](mpmovieplayertimedmetadatauserinfokey.md)
  An NSDictionary object containing the most recent `MPTimedMetadata` objects.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata)*