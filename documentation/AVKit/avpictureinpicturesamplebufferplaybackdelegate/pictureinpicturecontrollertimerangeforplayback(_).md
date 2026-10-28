# pictureInPictureControllerTimeRangeForPlayback(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for the current playable time range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func pictureInPictureControllerTimeRangeForPlayback(_ pictureInPictureController: AVPictureInPictureController) -> CMTimeRange
```

```objc
- (CMTimeRange) pictureInPictureControllerTimeRangeForPlayback:(AVPictureInPictureController *) pictureInPictureController;
```

## Return Value

A [`CMTimeRange`](../../CoreMedia/cmtimerange.md) value that defines the content’s time range.

## Discussion

Use the following guidelines when specifying a time range value:

- For live content, return a time range with a duration of [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md).
- For nonlive content, return a time range that contains the current time of the sample buffer display layer’s timebase.
- When there’s no content to play, return [`invalid`](../../CoreMedia/cmtimerange/invalid.md).

The system calls this method whenever you call the [`invalidatePlaybackState()`](../avpictureinpicturecontroller/invalidateplaybackstate%28%29.md) method, and at other times as it requires.

## Parameters

- `pictureInPictureController`: The Picture in Picture controller.

## See Also

### Responding to playback events
- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](./pictureinpicturecontroller%28_,setplaying%29.md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollerisplaybackpaused%28_%29.md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](./pictureinpicturecontroller%28_,didtransitiontorendersize%29.md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](./pictureinpicturecontroller%28_,skipbyinterval,completion%29.md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollershouldprohibitbackgroundaudioplayback%28_%29.md)
  Asks the delegate whether to always prohibit background audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:))*