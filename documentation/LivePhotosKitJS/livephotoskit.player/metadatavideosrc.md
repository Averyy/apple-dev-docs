# metadataVideoSrc

**Framework**: LivePhotosKit JS  
**Kind**: property

A string or array buffer that contains metadata about the properties of a Live Photo.

**Availability**:
- LivePhotosKit JS 1.3+

## Declaration

```swift
attribute String,ArrayBuffer metadataVideoSrc;
```

#### Discussion

If you have a video asset that does not include a readable [`photoTime`](livephotoskit.player/phototime.md) and/or [`frameTimes`](livephotoskit.player/frametimes.md), you can set this property to a string URL or ArrayBuffer referencing the original MOV file that was captured by an iPhone.  That file is then parsed in the same manner as those loaded thorough [`videoSrc`](livephotoskit.player/videosrc.md). It serves as an alternate source for the [`photoTime`](livephotoskit.player/phototime.md) and [`frameTimes`](livephotoskit.player/frametimes.md) properties if they are not otherwise available.

If this property is set to a URL, the file referred to by the URL is loaded only until the point at which  [`frameTimes`](livephotoskit.player/frametimes.md) and [`photoTime`](livephotoskit.player/phototime.md) can be determined from it.  The network request is then terminated early to avoid downloading unneeded data. Using this feature to allow the Player to automatically determine [`frameTimes`](livephotoskit.player/frametimes.md) and/or [`photoTime`](livephotoskit.player/phototime.md) may be easier than finding them yourself and providing them manually. However, it comes at the expense of an extra network request incurred by loading the beginning of the file.

You can set this property to an `ArrayBuffer` (for example, videoSrc or photoSrc). However, if you have an `ArrayBuffer` for the original video file, you can set that `ArrayBuffer` here to provide [`frameTimes`](livephotoskit.player/frametimes.md) and [`photoTime`](livephotoskit.player/phototime.md) values. An even simpler alternative is to just use that `ArrayBuffer` as the video source to begin with. (If you supply an `ArrayBuffer` here instead of a URL, there will be no network request, and no performance cost.)

The performance implications of using this property on a small page viewed by audiences with reliable, low-latency connections are probably minimal. However, do not use this approach when performance is critical.

> **Note**:  In typical circumstances, you can safely ignore this property.

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

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/metadatavideosrc)*