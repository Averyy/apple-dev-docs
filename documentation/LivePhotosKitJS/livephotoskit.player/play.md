# play

**Framework**: LivePhotosKit JS  
**Kind**: method

Starts playback if the player is ready, or resumes playback if the player is paused.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
Boolean play();
```

#### Return Value

`true` if the player starts or resumes playback; otherwise, `false`.

#### Discussion

If the playback completes, this method fires the `ended` event. If the playback is paused (and not resumed) or stopped, the `ended` event is not fired.

## See Also

- [beginFinishingPlaybackEarly](livephotoskit.player/beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [pause](livephotoskit.player/pause.md)
  Pauses playback at the current time.
- [stop](livephotoskit.player/stop.md)
  Stops playback and rewinds to the current time of zero.
- [toggle](livephotoskit.player/toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.
- [updateSize](livephotoskit.player/updatesize.md)
  Updates the size of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/play)*