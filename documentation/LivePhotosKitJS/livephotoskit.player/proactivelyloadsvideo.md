# proactivelyLoadsVideo

**Framework**: LivePhotosKit JS  
**Kind**: property

A boolean value that indicates whether the Player downloads bytes before the user begins playback.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute Boolean proactivelyLoadsVideo;
```

#### Discussion

Whether or not the Player downloads bytes at the provided [`videoSrc`](livephotoskit.player/videosrc.md) before the user begins playback.

If there are many Players on a page, a value of `false` enables configuration of [`videoSrc`](livephotoskit.player/videosrc.md) on all Players without forcing expensive downloads of each Player’s video asset.

If there are few Players on a page, a value of `true` decreases the warmup and loading time necessary after an attempt to initiate playback before playback actually begins.

This tradeoff is left to the developer, but in the interests of out-of-the-box scalability, this property defaults to `false`.

Declarative markup attribute: `data-proactively-loads-video`

## See Also

- [currentTime](livephotoskit.player/currenttime.md)
  The current time, in seconds, of the play head.
- [duration](livephotoskit.player/duration.md)
  The duration, in seconds, of the entire Live Photo.
- [photoHeight](livephotoskit.player/photoheight.md)
  The height, in pixels, of the photo component.
- [photoTime](livephotoskit.player/phototime.md)
  The nominated time, in seconds, of where the photo component should be within the Live Photo video component.
- [photoWidth](livephotoskit.player/photowidth.md)
  The width, in pixels, of the photo component.
- [canPlay](livephotoskit.player/canplay.md)
  A Boolean value that indicates whether the Player is able to begin playback.
- [errors](livephotoskit.player/errors.md)
  An array of errors that occurred when attempting to load resources.
- [frameTimes](livephotoskit.player/frametimes.md)
  An array of timestamps for each second from the beginning of a Live Photo for which the frames reside in the Live Photo.
- [isPlaying](livephotoskit.player/isplaying.md)
  A Boolean value that indicates whether or not the Player is playing.
- [loadProgress](livephotoskit.player/loadprogress.md)
  A numeric value that indicates the progress of loading the Live Photo.
- [metadataVideoSrc](livephotoskit.player/metadatavideosrc.md)
  A string or array buffer that contains metadata about the properties of a Live Photo.
- [photo](livephotoskit.player/photo.md)
  The renderable, image-bearing DOM element (either an image or a canvas) that the Player consumes to render itself to the screen.
- [photoMimeType](livephotoskit.player/photomimetype.md)
  The MIME type of a photo asset.
- [photoSrc](livephotoskit.player/photosrc.md)
  The source of the photo component of the Live Photo.
- [playbackStyle](livephotoskit.player/playbackstyle.md)
  The style of playback that determines the nature of an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/proactivelyloadsvideo)*