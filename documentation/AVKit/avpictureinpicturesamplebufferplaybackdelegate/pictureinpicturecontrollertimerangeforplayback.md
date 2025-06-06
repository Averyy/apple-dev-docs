# pictureInPictureControllerTimeRangeForPlayback(_:)

**Framework**: AVKit  
**Kind**: method  
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

#### Return Value

A [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) value that defines the content’s time range.

#### Discussion

Use the following guidelines when specifying a time range value:

- For live content, return a time range with a duration of [`positiveInfinity`](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity).
- For nonlive content, return a time range that contains the current time of the sample buffer display layer’s timebase.
- When there’s no content to play, return [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange/invalid).

The system calls this method whenever you call the [`invalidatePlaybackState()`](avpictureinpicturecontroller/invalidateplaybackstate().md) method, and at other times as it requires.

## Parameters

- `pictureInPictureController`: The Picture in Picture controller.

## See Also

- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:setplaying:).md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(_:).md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:).md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:).md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(_:).md)
  Asks the delegate whether to always prohibit background audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:))*