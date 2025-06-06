# videoMimeType

**Framework**: LivePhotosKit JS  
**Kind**: property

The MIME type of the video asset.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute String videoMimeType;
```

#### Discussion

The `MIME` type of the video asset, either as detected from a network request for the asset (if it was provided as a URL on [`videoSrc`](livephotoskit.player/videosrc.md)) or as provided by the developer prior to assigning a prepared `ArrayBuffer` to [`videoSrc`](livephotoskit.player/videosrc.md).

This property, while writable, behaves as read-only if the video was obtained through a network request to a string URL set on [`videoSrc`](livephotoskit.player/videosrc.md). In this case, writes to this property are ignored.

However, if the intent is to provide the video by assigning an already-loaded `ArrayBuffer` to [`videoSrc`](livephotoskit.player/videosrc.md), you must set this property to the correct MIME type beforehand.

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

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/videomimetype)*