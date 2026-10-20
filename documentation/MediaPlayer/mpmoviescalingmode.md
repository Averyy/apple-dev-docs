# MPMovieScalingMode

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

Constants describing how the movie content is scaled to fit the frame of its view.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
enum MPMovieScalingMode
```

```c
enum MPMovieScalingMode : NSInteger;
```

## Topics

### Constants
- [MPMovieScalingMode.none](./mpmoviescalingmode/none.md)
  Do not scale the movie.
- [MPMovieScalingMode.aspectFit](./mpmoviescalingmode/aspectfit.md)
  Scale the movie uniformly until one dimension fits the visible bounds of the view exactly. In the other dimension, the region between the edge of the movie and the edge of the view is filled with a black bar. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.aspectFill](./mpmoviescalingmode/aspectfill.md)
  Scale the movie uniformly until the movie fills the visible bounds of the view. Content at the edges of the larger of the two dimensions is clipped so that the other dimension fits the view exactly. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.fill](./mpmoviescalingmode/fill.md)
  Scale the movie until both dimensions fit the visible bounds of the view exactly. The aspect ratio of the movie is not preserved.
### Initializers
- [init?(rawValue: Int)](./mpmoviescalingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct MPMovieLoadState](./mpmovieloadstate.md)
  Constants describing the network load state of the movie player.
- [enum MPMovieControlStyle](./mpmoviecontrolstyle.md)
  Constants describing the style of the playback controls.
- [enum MPMovieFinishReason](./mpmoviefinishreason.md)
  Constants describing the reason that playback ended.
- [enum MPMoviePlaybackState](./mpmovieplaybackstate.md)
  Constants describing the current playback state of the movie player.
- [enum MPMovieRepeatMode](./mpmovierepeatmode.md)
  Constants describing how the movie player repeats content at the end of playback.
- [enum MPMovieTimeOption](./mpmovietimeoption.md)
  Constants describing which frame to use when generating thumbnail images.
- [struct MPMovieMediaTypeMask](./mpmoviemediatypemask.md)
  The types of content available in the movie file.
- [enum MPMovieSourceType](./mpmoviesourcetype.md)
  Specifies the type of the movie file.
- [Thumbnail notification user info keys](./thumbnail-notification-user-info-keys.md)
  The following keys may be found in the `userInfo` dictionary of a [`MPMoviePlayerThumbnailImageRequestDidFinishNotification`](./mpmovieplayerthumbnailimagerequestdidfinishnotification.md) notification.
- [Fullscreen notification keys](./fullscreen-notification-keys.md)
  The following keys may be found in the `userInfo` dictionary of notifications for transitioning in or out of full-screen mode.
- [Playback finished notification key](./playback-finished-notification-key.md)
  The following key may be found in the userInfo dictionary of a [`MPMoviePlayerPlaybackDidFinishNotification`](./mpmovieplayerplaybackdidfinishnotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode)*