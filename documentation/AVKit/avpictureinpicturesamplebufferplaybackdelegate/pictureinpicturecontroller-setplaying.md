# pictureInPictureController(_:setPlaying:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user requested to begin or pause playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, setPlaying playing: Bool)
```

## Parameters

- `pictureInPictureController`: The Picture in Picture controller.
- `playing`: A Boolean value that indicates whether to begin or pause playback.

## See Also

- [func pictureInPictureControllerTimeRangeForPlayback(AVPictureInPictureController) -> CMTimeRange](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:).md)
  Asks the delegate for the current playable time range.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(_:).md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:).md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:).md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(_:).md)
  Asks the delegate whether to always prohibit background audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:setplaying:))*