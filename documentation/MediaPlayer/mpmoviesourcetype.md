# MPMovieSourceType

**Framework**: Media Player  
**Kind**: enum

Specifies the type of the movie file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MPMovieSourceType
```

## Topics

### Constants
- [MPMovieSourceType.unknown](mpmoviesourcetype/unknown.md)
- [MPMovieSourceType.file](mpmoviesourcetype/file.md)
- [MPMovieSourceType.streaming](mpmoviesourcetype/streaming.md)
### Initializers
- [init?(rawValue: Int)](mpmoviesourcetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [Thumbnail notification user info keys](thumbnail-notification-user-info-keys.md)
  The following keys may be found in the `userInfo` dictionary of a [`MPMoviePlayerThumbnailImageRequestDidFinishNotification`](mpmovieplayerthumbnailimagerequestdidfinishnotification.md) notification.
- [Fullscreen notification keys](fullscreen-notification-keys.md)
  The following keys may be found in the `userInfo` dictionary of notifications for transitioning in or out of full-screen mode.
- [Playback finished notification key](playback-finished-notification-key.md)
  The following key may be found in the userInfo dictionary of a [`MPMoviePlayerPlaybackDidFinishNotification`](mpmovieplayerplaybackdidfinishnotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype)*