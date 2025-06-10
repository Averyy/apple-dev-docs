# pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(_:)

**Framework**: AVKit  
**Kind**: method

Asks the delegate whether to always prohibit background audio playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(_ pictureInPictureController: AVPictureInPictureController) -> Bool
```

#### Return Value

`true` if the delegate prohibits background audio playback; otherwise, `false`.

#### Discussion

If you implement this method, the system calls it once for each invocation of [`invalidatePlaybackState()`](avpictureinpicturecontroller/invalidateplaybackstate().md) to determine whether to prohibit audio playback when the Picture in Picture window is in the background.

## Parameters

- `pictureInPictureController`: The Picture in Picture controller instance.

## See Also

- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:setplaying:).md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerTimeRangeForPlayback(AVPictureInPictureController) -> CMTimeRange](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:).md)
  Asks the delegate for the current playable time range.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(_:).md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:).md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:).md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(_:))*