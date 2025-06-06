# updateSize

**Framework**: LivePhotosKit JS  
**Kind**: method

Updates the size of the player.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
void updateSize();
```

#### Discussion

Call this method when the size of the element changes—for example, when you change the size directly or when the element size changes depending on the layout of other elements. Also call this method when attaching the player to the DOM or changing the `display` style from `none`. Since the player handles window resize events itself, you don’t need to call this method when the window size changes.

## Parameters

- `forceOrDisplayWidth`: If a Boolean value, indicates whether the player should be forced to render. If a number value, specifies the width of the player.
- `displayHeight`: The height of the player. The default uses the photo’s aspect ratio to calculate the display height.

## See Also

- [beginFinishingPlaybackEarly](livephotoskit.player/beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [pause](livephotoskit.player/pause.md)
  Pauses playback at the current time.
- [play](livephotoskit.player/play.md)
  Starts playback if the player is ready, or resumes playback if the player is paused.
- [stop](livephotoskit.player/stop.md)
  Stops playback and rewinds to the current time of zero.
- [toggle](livephotoskit.player/toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/updatesize)*