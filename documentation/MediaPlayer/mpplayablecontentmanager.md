# MPPlayableContentManager

**Framework**: Media Player  
**Kind**: class

A shared content manager for controlling interactions between your media app and system-provided or external media player interfaces.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPPlayableContentManager
```

#### Overview

> ❗ **Important**:  Some features of this class are specific to CarPlay, which requires a special entitlement issued by Apple. Apps without the correct entitlement won’t appear on the CarPlay home screen. See [`http://www.apple.com/ios/carplay/`](https://developer.apple.comhttp://www.apple.com/ios/carplay/) for more information.

 Some features of this class are specific to CarPlay, which requires a special entitlement issued by Apple. Apps without the correct entitlement won’t appear on the CarPlay home screen. See [`http://www.apple.com/ios/carplay/`](https://developer.apple.comhttp://www.apple.com/ios/carplay/) for more information.

The app provides data to the content manager so that the media player can browse the content provided. A delegate provides the media player the ability to perform actions that manage the app’s playback queue.

You don’t create a new content manager directly, instead you grab the shared content manager using the [`shared()`](mpplayablecontentmanager/shared().md) method. After getting the shared content manager, your next step depends on the features your app supports:

- To provide content navigation and suggested content for CarPlay, immediately set both the [`dataSource`](mpplayablecontentmanager/datasource.md) and [`delegate`](mpplayablecontentmanager/delegate.md) properties. After setting these properties, use the [`beginUpdates()`](mpplayablecontentmanager/beginupdates().md) and [`endUpdates()`](mpplayablecontentmanager/endupdates().md) methods to load the information from the data source.
- To provide suggested content when the user connects headphones, a Bluetooth stereo, or another output device, set only the [`delegate`](mpplayablecontentmanager/delegate.md) property. After you set a delegate, iOS automatically calls methods in the [`MPPlayableContentDelegate`](mpplayablecontentdelegate.md) protocol allowing you to suggest appropriate content.

## Topics

### Providing playable content
- [var dataSource: (any MPPlayableContentDataSource)?](mpplayablecontentmanager/datasource.md)
  The data source provided by the app.
- [protocol MPPlayableContentDataSource](mpplayablecontentdatasource.md)
  The data source providing media metadata to external media players so they can build user interfaces displaying your app’s content.
### Responding to playback events
- [var delegate: (any MPPlayableContentDelegate)?](mpplayablecontentmanager/delegate.md)
  A delegate that lets the media player manage the app’s playback queue.
- [protocol MPPlayableContentDelegate](mpplayablecontentdelegate.md)
  The protocol used to let external media players send playback commands to an app.
### Setting the content manager
- [class func shared() -> Self](mpplayablecontentmanager/shared.md)
  Returns the current content manager instance.
### Updating data
- [func beginUpdates()](mpplayablecontentmanager/beginupdates.md)
  Updates several Media Player content items at once.
- [func endUpdates()](mpplayablecontentmanager/endupdates.md)
  Ends a synchronized update.
- [func reloadData()](mpplayablecontentmanager/reloaddata.md)
  Reloads the data from the data source.
### Retrieving information on currently playing items
- [var context: MPPlayableContentManagerContext](mpplayablecontentmanager/context.md)
  The current state of the playable content endpoint.
- [var nowPlayingIdentifiers: [String]](mpplayablecontentmanager/nowplayingidentifiers.md)
  The content items currently playing based on their identifiers.

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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager)*