# pause

**Framework**: LivePhotosKit JS  
**Kind**: method  
**Role**: Instance Method

Pauses playback at the current time.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```
void pause();
```

#### Discussion

This ensures that [`wantsToPlay`](./wantstoplay.md) is `false`, meaning that if loading activity completes, playback will not begin spuriously.

If the Player is already not playing, then, aside from maintaining the [`wantsToPlay`](./wantstoplay.md) value, this does nothing.

To resume playback, call the [`play`](./play.md) or [`toggle`](./toggle.md) method.

## See Also

### Instance Methods
- [beginFinishingPlaybackEarly](./beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [play](./play.md)
  Starts playback if the player is ready, or resumes playback if the player is paused.
- [stop](./stop.md)
  Stops playback and rewinds to the current time of zero.
- [toggle](./toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.
- [updateSize](./updatesize.md)
  Updates the size of the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/pause)*