# MPMoviePlayerController

**Framework**: Media Player  
**Kind**: class

A type of movie player that manages the playback of a movie from a file or a network stream.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
class MPMoviePlayerController
```

#### Overview

> ❗ **Important**:  The [`MPMoviePlayerController`](mpmovieplayercontroller.md) class is formally deprecated in iOS 9. (The [`MPMoviePlayerViewController`](mpmovieplayerviewcontroller.md) class is also formally deprecated.) To play video content in iOS 9 and later, instead use the [`AVPictureInPictureController`](https://developer.apple.com/documentation/AVKit/AVPictureInPictureController) or [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) class from the AVKit framework, or the [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) class from WebKit.

Playback occurs in a view owned by the movie player and takes place either fullscreen or inline. You can incorporate a movie player’s view into a view hierarchy owned by your app, or use an MPMoviePlayerViewController object to manage the presentation for you.

Movie players support wireless movie playback to AirPlay-enabled hardware such as Apple TV. AirPlay playback is enabled by default. To disable AirPlay in your app, set the [`allowsAirPlay`](mpmovieplayercontroller/allowsairplay.md) property to [`false`](https://developer.apple.com/documentation/Swift/false). In iOS 8.0 and later, users access AirPlay compatible hardware through the Control Panel; no AirPlay control is displayed by the movie player.

When you add a movie player’s view to your app’s view hierarchy, be sure to size the frame correctly, as shown here:

```objc
MPMoviePlayerController *player =
        [[MPMoviePlayerController alloc] initWithContentURL: myURL];
[player prepareToPlay];
[player.view setFrame: myView.bounds];  // player's frame must match parent's
[myView addSubview: player.view];
// ...
[player play];
```

Consider a movie player view to be an opaque structure. You can add your own custom subviews to layer content on top of the movie but you must never modify any of its existing subviews.

In addition to layering content on top of a movie, you can provide custom background content by adding subviews to the view in the [`backgroundView`](mpmovieplayercontroller/backgroundview.md) property. Custom subviews are supported in both inline and fullscreen playback modes but you must adjust the positions of your views when entering or exiting fullscreen mode. Use the [`MPMoviePlayerWillEnterFullscreenNotification`](mpmovieplayerwillenterfullscreennotification.md) and [`MPMoviePlayerWillExitFullscreenNotification`](mpmovieplayerwillexitfullscreennotification.md) notifications to detect changes to and from fullscreen mode.

This class supports programmatic control of movie playback, and user-based control via buttons supplied by the movie player. You can control most aspects of playback programmatically using the methods and properties of the [`MPMediaPlayback`](mpmediaplayback.md) protocol, to which this class conforms. The methods and properties of that protocol let you start and stop playback, seek forward and backward through the movie’s content, and even change the playback rate. In addition, the [`controlStyle`](mpmovieplayercontroller/controlstyle.md) property of this class lets you display a set of standard system controls that allow the user to manipulate playback. You can also set the [`shouldAutoplay`](mpmovieplayercontroller/shouldautoplay.md) property for network-based content to start automatically.

You typically specify the movie you want to play when you create a new `MPMoviePlayerController` object. However, you can also change the currently playing movie by changing the value in the [`contentURL`](mpmovieplayercontroller/contenturl.md) property. Changing this property lets you reuse the same movie player controller object in multiple places. For performance reasons you may want to play movies as local files. Do this by first downloading them to a local directory.

> **Note**:  Although you can create multiple `MPMoviePlayerController` objects and present their views in your interface, only one movie player at a time can play its movie.

To facilitate the creation of video bookmarks or chapter links for a long movie, the `MPMoviePlayerController` class defines methods for generating thumbnail images at specific times within a movie. You can request a single thumbnail image using the [`thumbnailImage(atTime:timeOption:)`](mpmovieplayercontroller/thumbnailimage(attime:timeoption:).md) method or request multiple thumbnail images using the [`requestThumbnailImages(atTimes:timeOption:)`](mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:).md) method.

To play a network stream whose URL requires access credentials, first create an appropriate [`URLCredential`](https://developer.apple.com/documentation/Foundation/URLCredential) object. Do this by calling, for example, the [`init(user:password:persistence:)`](https://developer.apple.com/documentation/Foundation/URLCredential/init(user:password:persistence:)) method, as shown here:

```objc
NSURLCredential *credential = [[NSURLCredential alloc]
                        initWithUser: @"userName"
                            password: @"password"
                         persistence: NSURLCredentialPersistenceForSession];
 
self.credential = credential;
[credential release];
```

In addition, create an appropriate [`URLProtectionSpace`](https://developer.apple.com/documentation/Foundation/URLProtectionSpace) object, as shown here. Make appropriate modifications for the realm you are accessing:

```objc
NSURLProtectionSpace *protectionSpace = [[NSURLProtectionSpace alloc]
                            initWithHost: "@streams.mydomain.com"
                                    port: 80
                                protocol: @"http"
                                   realm: @"mydomain.com"
                    authenticationMethod: NSURLAuthenticationMethodDefault];
 
self.protectionSpace = protectionSpace;
[protectionSpace release];
```

Add the URL credential and the protection space to the [`Singleton`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49) [`URLCredentialStorage`](https://developer.apple.com/documentation/Foundation/URLCredentialStorage) object. Do this by calling, for example, the [`set(_:for:)`](https://developer.apple.com/documentation/Foundation/URLCredentialStorage/set(_:for:)) method, as shown here:

```objc
[[NSURLCredentialStorage sharedCredentialStorage]
                    setDefaultCredential: credential
                      forProtectionSpace: protectionSpace];
```

With the credential and protection space information in place, you can then play the protected stream.

##### Movie Player Notifications

A movie player generates notifications to keep your app informed about the state of movie playback. In addition to being notified when playback finishes, your app can be notified in the following situations:

- When the movie player begins playing, is paused, or begins seeking forward or backward
- When AirPlay playback starts or ends
- When the scaling mode of the movie changes
- When the movie enters or exits fullscreen mode
- When the load state for network-based movies changes
- When meta-information about the movie itself becomes available

For more information, see the Notifications section in this document.

## Topics

### Creating and initializing the object
- [init!(contentURL: URL!)](mpmovieplayercontroller/init(contenturl:).md)
  Returns a `MPMoviePlayerController` object initialized with the movie at the specified URL.
### Accessing movie properties
- [var contentURL: URL!](mpmovieplayercontroller/contenturl.md)
  The URL that points to the movie file.
- [var movieSourceType: MPMovieSourceType](mpmovieplayercontroller/moviesourcetype.md)
  The playback type of the movie.
- [var movieMediaTypes: MPMovieMediaTypeMask](mpmovieplayercontroller/moviemediatypes.md)
  The types of media available in the movie.
- [var allowsAirPlay: Bool](mpmovieplayercontroller/allowsairplay.md)
  Specifies whether the movie player allows AirPlay movie playback.
- [var isAirPlayVideoActive: Bool](mpmovieplayercontroller/isairplayvideoactive.md)
  Indicates whether the movie player is currently playing video via AirPlay.
- [var naturalSize: CGSize](mpmovieplayercontroller/naturalsize.md)
  The width and height of the movie frame.
- [var isFullscreen: Bool](mpmovieplayercontroller/isfullscreen.md)
  A Boolean that indicates whether the movie player is in full-screen mode.
- [func setFullscreen(Bool, animated: Bool)](mpmovieplayercontroller/setfullscreen(_:animated:).md)
  Causes the movie player to enter or exit full-screen mode.
- [var scalingMode: MPMovieScalingMode](mpmovieplayercontroller/scalingmode.md)
  The scaling mode to use when displaying the movie.
- [var controlStyle: MPMovieControlStyle](mpmovieplayercontroller/controlstyle.md)
  The style of the playback controls.
- [var useApplicationAudioSession: Bool](mpmovieplayercontroller/useapplicationaudiosession.md)
  A Boolean value that indicates whether the movie player should use the app’s audio session.
### Accessing the movie duration
- [var duration: TimeInterval](mpmovieplayercontroller/duration.md)
  The duration of the movie, measured in seconds.
- [var playableDuration: TimeInterval](mpmovieplayercontroller/playableduration.md)
  The amount of currently playable content.
### Accessing the view
- [var view: UIView!](mpmovieplayercontroller/view.md)
  The view containing the movie content and controls.
- [var backgroundView: UIView!](mpmovieplayercontroller/backgroundview.md)
  A customizable view that is displayed behind the movie content.
### Controlling and monitoring playback
- [var loadState: MPMovieLoadState](mpmovieplayercontroller/loadstate.md)
  The network load state of the movie player.
- [var playbackState: MPMoviePlaybackState](mpmovieplayercontroller/playbackstate.md)
  The current playback state of the movie player.
- [var initialPlaybackTime: TimeInterval](mpmovieplayercontroller/initialplaybacktime.md)
  The time, specified in seconds within the video timeline, when playback should start.
- [var endPlaybackTime: TimeInterval](mpmovieplayercontroller/endplaybacktime.md)
  The end time (measured in seconds) for playback of the movie.
- [var shouldAutoplay: Bool](mpmovieplayercontroller/shouldautoplay.md)
  A Boolean that indicates whether a movie should begin playback automatically.
- [var readyForDisplay: Bool](mpmovieplayercontroller/readyfordisplay.md)
  A Boolean that indicates whether the first video frame of the movie is ready to be displayed.
- [var repeatMode: MPMovieRepeatMode](mpmovieplayercontroller/repeatmode.md)
  Determines how the movie player repeats the playback of the movie.
- [var timedMetadata: [Any]!](mpmovieplayercontroller/timedmetadata.md)
  Obtains the most recent time-based metadata provided by the streamed movie.
### Generating thumbnail images
- [func thumbnailImage(atTime: TimeInterval, timeOption: MPMovieTimeOption) -> UIImage!](mpmovieplayercontroller/thumbnailimage(attime:timeoption:).md)
  Captures and returns a thumbnail image from the current movie.
- [func requestThumbnailImages(atTimes: [Any]!, timeOption: MPMovieTimeOption)](mpmovieplayercontroller/requestthumbnailimages(attimes:timeoption:).md)
  Captures one or more thumbnail images asynchronously from the current movie.
- [func cancelAllThumbnailImageRequests()](mpmovieplayercontroller/cancelallthumbnailimagerequests.md)
  Cancels all pending asynchronous thumbnail image requests.
### Retrieving movie logs
- [var accessLog: MPMovieAccessLog!](mpmovieplayercontroller/accesslog.md)
  A snapshot of the network playback log for the movie player if it is playing a network stream.
- [var errorLog: MPMovieErrorLog!](mpmovieplayercontroller/errorlog.md)
  A snapshot of the playback failure error log for the movie player if it is playing a network stream.
### Constants
- [struct MPMovieLoadState](mpmovieloadstate.md)
  Constants describing the network load state of the movie player.
- [enum MPMovieControlStyle](mpmoviecontrolstyle.md)
  Constants describing the style of the playback controls.
- [enum MPMovieFinishReason](mpmoviefinishreason.md)
  Constants describing the reason that playback ended.
- [enum MPMoviePlaybackState](mpmovieplaybackstate.md)
  Constants describing the current playback state of the movie player.
- [enum MPMovieRepeatMode](mpmovierepeatmode.md)
  Constants describing how the movie player repeats content at the end of playback.
- [enum MPMovieScalingMode](mpmoviescalingmode.md)
  Constants describing how the movie content is scaled to fit the frame of its view.
- [enum MPMovieTimeOption](mpmovietimeoption.md)
  Constants describing which frame to use when generating thumbnail images.
- [struct MPMovieMediaTypeMask](mpmoviemediatypemask.md)
  The types of content available in the movie file.
- [enum MPMovieSourceType](mpmoviesourcetype.md)
  Specifies the type of the movie file.
- [Thumbnail notification user info keys](thumbnail-notification-user-info-keys.md)
  The following keys may be found in the `userInfo` dictionary of a [`MPMoviePlayerThumbnailImageRequestDidFinishNotification`](mpmovieplayerthumbnailimagerequestdidfinishnotification.md) notification.
- [Fullscreen notification keys](fullscreen-notification-keys.md)
  The following keys may be found in the `userInfo` dictionary of notifications for transitioning in or out of full-screen mode.
- [Playback finished notification key](playback-finished-notification-key.md)
  The following key may be found in the userInfo dictionary of a [`MPMoviePlayerPlaybackDidFinishNotification`](mpmovieplayerplaybackdidfinishnotification.md) notification.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPMediaPlayback](mpmediaplayback.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)*