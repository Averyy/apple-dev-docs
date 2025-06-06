# photoSrc

**Framework**: LivePhotosKit JS  
**Kind**: property

The source of the photo component of the Live Photo.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute String,ArrayBuffer photoSrc;
```

#### Discussion

Set this property to three types of value:

- A String URL
- An `ArrayBuffer` instance that may already be available
- `null` (to clear the Player’s photo)

Changing this value causes the [`photo`](livephotoskit.player/photo.md) property (the image consumed by the Player for rendering) to be initially set to `null`. If the new value assigned is a string URL or an `ArrayBuffer`, a round of loading and decoding activity begins, eventually resulting in the [`photo`](livephotoskit.player/photo.md) property being populated with the newly loaded image. Only a string URL produces a network request as part of this loading process.

Changing this value while loading activity from a previous assignment is in progress causes the previous loading activity to abort.

Note: If, due to the architecture of your web app or web page, an already-loaded `Image` instance or fully painted canvas element is available, write it directly to the [`photo`](livephotoskit.player/photo.md) property instead.

Declarative markup attribute: `data-photo-src`

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
- [playbackStyle](livephotoskit.player/playbackstyle.md)
  The style of playback that determines the nature of an animation.
- [proactivelyLoadsVideo](livephotoskit.player/proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/photosrc)*