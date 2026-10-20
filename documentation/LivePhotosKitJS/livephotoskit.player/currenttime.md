# currentTime

**Framework**: LivePhotosKit JS  
**Kind**: property  
**Role**: Instance Property

The current time, in seconds, of the play head.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```
readonly attribute Number currentTime;
```

#### Discussion

Setting this property moves the play head synchronously to the specified time.

Allowable values are floating points between `0` and [`duration`](./duration.md). A value that places the play head between frames shows a weighted average of the two frames.

If the playback style is [`FULL`](../livephotoskit.playbackstyle/full.md) a value of `0` corresponds to the at-rest view of the full-resolution photo. As `currentTime` increases, the Live Photo animation will be played back according to the playback style.

Because the required frames might not be decoded, setting `currentTime` could fail. In this case, `currentTime` will not take on its just-assigned value. Setting `currentTime` again to the same value in the near future will most likely succeed. There is no asynchronous callback to test for when the missing requirements for a particular `currentTime` value become available.

## See Also

### Instance Properties
- [duration](./duration.md)
  The duration, in seconds, of the entire Live Photo.
- [photoHeight](./photoheight.md)
  The height, in pixels, of the photo component.
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

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/currenttime)*