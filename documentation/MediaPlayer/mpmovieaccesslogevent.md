# MPMovieAccessLogEvent

**Framework**: Media Player  
**Kind**: class

A single piece of information for a movie access log.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class MPMovieAccessLogEvent
```

#### Overview

For a description of movie access logs, see [`MPMovieAccessLog`](mpmovieaccesslog.md).

## Topics

### Movie access log event properties
- [var numberOfSegmentsDownloaded: Int](mpmovieaccesslogevent/numberofsegmentsdownloaded.md)
  A count of media segments downloaded from the web server to your app.
- [var playbackStartDate: Date!](mpmovieaccesslogevent/playbackstartdate.md)
  The timestamp for when playback began for the movie log access event.
- [var uri: String!](mpmovieaccesslogevent/uri.md)
  The URI of the playback item.
- [var serverAddress: String!](mpmovieaccesslogevent/serveraddress.md)
  The IPv4 or IPv6 address of the web server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](mpmovieaccesslogevent/numberofserveraddresschanges.md)
  A count of changes to the [`serverAddress`](mpmovieaccesslogevent/serveraddress.md) property over the last uninterrupted period of playback.
- [var playbackSessionID: String!](mpmovieaccesslogevent/playbacksessionid.md)
  A GUID that identifies the playback session to use in HTTP requests.
- [var playbackStartOffset: TimeInterval](mpmovieaccesslogevent/playbackstartoffset.md)
  An offset into the playlist where the last uninterrupted period of playback began, in seconds.
- [var segmentsDownloadedDuration: TimeInterval](mpmovieaccesslogevent/segmentsdownloadedduration.md)
  The accumulated duration of the media downloaded, in seconds.
- [var durationWatched: TimeInterval](mpmovieaccesslogevent/durationwatched.md)
  The accumulated duration of the media played, in seconds.
- [var numberOfStalls: Int](mpmovieaccesslogevent/numberofstalls.md)
  The total number of playback stalls encountered.
- [var numberOfBytesTransferred: Int64](mpmovieaccesslogevent/numberofbytestransferred.md)
  The accumulated number of bytes transferred.
- [var observedBitrate: Double](mpmovieaccesslogevent/observedbitrate.md)
  The empirical throughput across all media downloaded for the movie player, in bits per second.
- [var indicatedBitrate: Double](mpmovieaccesslogevent/indicatedbitrate.md)
  The throughput required to play the stream, as advertised by the web server, in bits per second.
- [var numberOfDroppedVideoFrames: Int](mpmovieaccesslogevent/numberofdroppedvideoframes.md)
  The total number of dropped video frames.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPMovieAccessLog](mpmovieaccesslog.md)
  Key metrics about network playback for an associated movie player that’s playing streamed content.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent)*