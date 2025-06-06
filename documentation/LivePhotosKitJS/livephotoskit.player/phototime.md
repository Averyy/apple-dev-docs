# photoTime

**Framework**: LivePhotosKit JS  
**Kind**: property

The nominated time, in seconds, of where the photo component should be within the Live Photo video component.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
attribute Number photoTime;
```

#### Discussion

This is the timestamp, in seconds from the beginning of the provided video asset, at which the still photo was captured.

This value is required to properly play back the Live Photo; without it, the Player is unable to play.

The Player does its best to make getting this value populated as easy as possible. There are a few ways to provide this value:

- If you provide the video by assigning videoSrc, and you use the original QuickTime MOV captured by iPhone, this value will be discovered and populated automatically as part of the loading process.
- If you provide a URL or ArrayBuffer for the original QuickTime MOV to the metadataVideoSrc property, the asset will be loaded just far enough to provide this value automatically. Note that this is a convenience, and performance-critical uses may wish to avoid incurring the extra network request.
- Failing both of the above two options, the value for this photoTime property must be assigned manually.

Declarative markup attribute: `data-photo-time`

## See Also

- [currentTime](livephotoskit.player/currenttime.md)
  The current time, in seconds, of the play head.
- [duration](livephotoskit.player/duration.md)
  The duration, in seconds, of the entire Live Photo.
- [photoHeight](livephotoskit.player/photoheight.md)
  The height, in pixels, of the photo component.
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
- [proactivelyLoadsVideo](livephotoskit.player/proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/phototime)*