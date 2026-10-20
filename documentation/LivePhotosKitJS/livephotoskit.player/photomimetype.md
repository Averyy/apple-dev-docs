# photoMimeType

**Framework**: LivePhotosKit JS  
**Kind**: property  
**Role**: Instance Property

The MIME type of a photo asset.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```
attribute String photoMimeType;
```

#### Discussion

The `MIME` type is either as detected from a network request for the asset (if the `MIME` type was provided as a URL on [`photoSrc`](./photosrc.md)) or as provided by the developer prior to assigning a prepared `ArrayBuffer` to [`photoSrc`](./photosrc.md).

This property, while writable, behaves as read-only if the photo was obtained through a network request to a string URL set on [`photoSrc`](./photosrc.md). In this case, writes to this property are ignored.

However, if the intent is to assign an already loaded `ArrayBuffer` to [`photoSrc`](./photosrc.md), you must set this property to the correct MIME type beforehand. This type is usually `image/jpeg`, but can vary if you provide a different image format. In that case, the property defaults to the value `image/jpeg`.

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
- [photoSrc](./photosrc.md)
  The source of the photo component of the Live Photo.
- [playbackStyle](./playbackstyle.md)
  The style of playback that determines the nature of an animation.
- [proactivelyLoadsVideo](./proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/photomimetype)*