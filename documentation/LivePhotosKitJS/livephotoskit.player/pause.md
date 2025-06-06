# pause

**Framework**: LivePhotosKit JS  
**Kind**: method

Pauses playback at the current time.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
void pause();
```

#### Discussion

This ensures that [`wantsToPlay`](livephotoskit.player/wantstoplay.md) is `false`, meaning that if loading activity completes, playback will not begin spuriously.

If the Player is already not playing, then, aside from maintaining the [`wantsToPlay`](livephotoskit.player/wantstoplay.md) value, this does nothing.

To resume playback, call the [`play`](livephotoskit.player/play.md) or [`toggle`](livephotoskit.player/toggle.md) method.

## See Also

- [beginFinishingPlaybackEarly](livephotoskit.player/beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [play](livephotoskit.player/play.md)
  Starts playback if the player is ready, or resumes playback if the player is paused.
- [stop](livephotoskit.player/stop.md)
  Stops playback and rewinds to the current time of zero.
- [toggle](livephotoskit.player/toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.
- [updateSize](livephotoskit.player/updatesize.md)
  Updates the size of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/pause)*