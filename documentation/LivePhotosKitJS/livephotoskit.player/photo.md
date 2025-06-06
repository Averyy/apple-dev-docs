# photo

**Framework**: LivePhotosKit JS  
**Kind**: property

The renderable, image-bearing DOM element (either an image or a canvas) that the Player consumes to render itself to the screen.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute HTMLImageElement,HTMLCanvasElement photo;
```

#### Discussion

If this property is not populated by an image or canvas, the Player cannot play or render.

You can provide a value for this property in one of several ways:

- Set [`photoSrc`](livephotoskit.player/photosrc.md) to a string URL and wait for the resulting download and decode to complete, at which point the property is populated with the resulting image.
- Set [`photoSrc`](livephotoskit.player/photosrc.md) to an `ArrayBuffer` and wait for the decode to complete, at which point the property is populated with the resulting image.
- Set the property directly to a fully loaded `HTMLImageElement` (such that its `complete` property is `true`).
- Set the property directly to an `HTMLCanvasElement` you have prepared, such that its backing store depicts the photo and that the photo is scaled properly.

Assigning this property directly causes [`photoSrc`](livephotoskit.player/photosrc.md) to be cleared and set back to `null`. Moreover, if [`photoSrc`](livephotoskit.player/photosrc.md) was recently assigned and a network request or asynchronous decoding is still happening; that activity is also canceled.

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
- [photoMimeType](livephotoskit.player/photomimetype.md)
  The MIME type of a photo asset.
- [photoSrc](livephotoskit.player/photosrc.md)
  The source of the photo component of the Live Photo.
- [playbackStyle](livephotoskit.player/playbackstyle.md)
  The style of playback that determines the nature of an animation.
- [proactivelyLoadsVideo](livephotoskit.player/proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/photo)*