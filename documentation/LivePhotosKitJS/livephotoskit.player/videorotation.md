# videoRotation

**Framework**: LivePhotosKit JS  
**Kind**: property

The angle that the video is displayed.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute Number videoRotation;
```

#### Discussion

This property takes on a value of: 0, 90, 180, or 270, and is automatically determined as part of the video loading process.

A video might be provided in a different format, and that video is rotated in a way that the Player or the browser can’t compensate for. In this situation, you can manually assign a different value to correct the issue without having to rotate the source video.

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

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/videorotation)*