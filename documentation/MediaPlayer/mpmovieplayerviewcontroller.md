# MPMoviePlayerViewController

**Framework**: Media Player  
**Kind**: class

A simple view controller for displaying full-screen movies.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class MPMoviePlayerViewController
```

#### Overview

> ❗ **Important**:  The [`MPMoviePlayerViewController`](mpmovieplayerviewcontroller.md) class is formally deprecated in iOS 9. (The [`MPMoviePlayerController`](mpmovieplayercontroller.md) class is also formally deprecated.) To play video content in iOS 9 and later, instead use the [`AVPictureInPictureController`](https://developer.apple.com/documentation/AVKit/AVPictureInPictureController) or [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class from the AVKit framework, or the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class from WebKit.

 The [`MPMoviePlayerViewController`](mpmovieplayerviewcontroller.md) class is formally deprecated in iOS 9. (The [`MPMoviePlayerController`](mpmovieplayercontroller.md) class is also formally deprecated.) To play video content in iOS 9 and later, instead use the [`AVPictureInPictureController`](https://developer.apple.com/documentation/AVKit/AVPictureInPictureController) or [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class from the AVKit framework, or the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class from WebKit.

Unlike using an [`MPMoviePlayerController`](mpmovieplayercontroller.md) object on its own to present a movie immediately, you can incorporate a movie player view controller wherever you would normally use a view controller. For example, you can present it using a tab bar or navigation bar-based interface, taking advantage of the transitions offered by those interfaces.

To present a movie player view controller modally, you typically use the [`presentMoviePlayerViewControllerAnimated(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/presentMoviePlayerViewControllerAnimated(_:)) method. This method is part of a category on the [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) class and is implemented by the Media Player framework. The [`presentMoviePlayerViewControllerAnimated(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/presentMoviePlayerViewControllerAnimated(_:)) method presents a movie player view controller using the standard transition animations for presenting video content. To dismiss a modally presented movie player view controller, call the [`dismissMoviePlayerViewControllerAnimated()`](https://developer.apple.com/documentation/UIKit/UIViewController/dismissMoviePlayerViewControllerAnimated()) method.

## Topics

### New methods
- [init!(contentURL: URL!)](mpmovieplayerviewcontroller/init(contenturl:).md)
  Returns a movie player view controller initialized with the specified movie.
- [var moviePlayer: MPMoviePlayerController!](mpmovieplayerviewcontroller/movieplayer.md)
  The movie player controller object used to present the movie.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller)*