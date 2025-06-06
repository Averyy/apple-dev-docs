# stop

**Framework**: LivePhotosKit JS  
**Kind**: method

Stops playback and rewinds to the current time of zero.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
void stop();
```

#### Discussion

After this method is called, the [`currentTime`](livephotoskit.player/currenttime.md) property is `0`. Like [`pause`](livephotoskit.player/pause.md), this causes [`wantsToPlay`](livephotoskit.player/wantstoplay.md) to become `false`.

## See Also

- [beginFinishingPlaybackEarly](livephotoskit.player/beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [pause](livephotoskit.player/pause.md)
  Pauses playback at the current time.
- [play](livephotoskit.player/play.md)
  Starts playback if the player is ready, or resumes playback if the player is paused.
- [toggle](livephotoskit.player/toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.
- [updateSize](livephotoskit.player/updatesize.md)
  Updates the size of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/stop)*