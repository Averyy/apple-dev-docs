# photoHeight

**Framework**: LivePhotosKit JS  
**Kind**: property  
**Role**: Instance Property

The height, in pixels, of the photo component.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```
readonly attribute Number photoHeight;
```

#### Discussion

Height of the photo component (as obtained from [`photoSrc`](./photosrc.md) or [`photo`](./photo.md)) in pixels.

## See Also

### Instance Properties
- [currentTime](./currenttime.md)
  The current time, in seconds, of the play head.
- [duration](./duration.md)
  The duration, in seconds, of the entire Live Photo.
- [photoTime](./phototime.md)
  The nominated time, in seconds, of where the photo component should be within the Live Photo video component.
- [photoWidth](./photowidth.md)
  The width, in pixels, of the photo component.
- [canPlay](./canplay.md)
  A Boolean value that indicates whether the Player is able to begin playback.
- [errors](./errors.md)
  An array of errors that occurred when attempting to load resources.
- [frameTimes](./frametimes.md)
  An array of timestamps for each second from the beginning of a Live Photo for which the frames reside in the Live Photo.
- [isPlaying](./isplaying.md)
  A Boolean value that indicates whether or not the Player is playing.
- [loadProgress](./loadprogress.md)
  A numeric value that indicates the progress of loading the Live Photo.
- [metadataVideoSrc](./metadatavideosrc.md)
  A string or array buffer that contains metadata about the properties of a Live Photo.
- [photo](./photo.md)
  The renderable, image-bearing DOM element (either an image or a canvas) that the Player consumes to render itself to the screen.
- [photoMimeType](./photomimetype.md)
  The MIME type of a photo asset.
- [photoSrc](./photosrc.md)
  The source of the photo component of the Live Photo.
- [playbackStyle](./playbackstyle.md)
  The style of playback that determines the nature of an animation.
- [proactivelyLoadsVideo](./proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/photoheight)*