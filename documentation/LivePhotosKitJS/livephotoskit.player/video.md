# video

**Framework**: LivePhotosKit JS  
**Kind**: property  
**Role**: Instance Property

The playable `HTMLVideoElement` that the Player consumes to obtain video frame data to render to the screen while animating a Live Photo.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```
attribute HTMLVideoElement video;
```

#### Discussion

If this property is not populated by a playable `HTMLVideoElement`, the Player cannot play, but can still render as a photo if `photo` is populated.

You can get a value for this property in one of a few ways:

- Set [`videoSrc`](./videosrc.md) to a string URL and wait for the resulting download and preparation to complete, at which point the property is populated with the resulting `HTMLVideoElement`.
- Set the [`videoSrc`](./videosrc.md) to an `ArrayBuffer` and wait for the resulting preparation to complete, at which point the property is populated with the resulting `HTMLVideoElement`.
- Set the property directly to a fully playable `HTMLVideoElement` whose `canplay` event has fired.

Assigning this property directly causes [`videoSrc`](./videosrc.md) to be cleared and set back to `null`. Moreover, if [`videoSrc`](./videosrc.md) was recently assigned and a network request or asynchronous decoding is still happening, that activity is also canceled.

## See Also

### Instance Properties
- [currentTime](./currenttime.md)
  The current time, in seconds, of the play head.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/video)*