# pictureInPictureController(_:didTransitionToRenderSize:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when the system Picture in Picture window changes size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, didTransitionToRenderSize newRenderSize: CMVideoDimensions)
```

```objc
- (void) pictureInPictureController:(AVPictureInPictureController *) pictureInPictureController didTransitionToRenderSize:(CMVideoDimensions) newRenderSize;
```

## Discussion

Take the new render size and the [`isPictureInPictureActive`](../avpictureinpicturecontroller/ispictureinpictureactive.md) state into account when choosing media variants to avoid uncessary decoding overhead.

## Parameters

- `pictureInPictureController`: The Picture in Picture controller.
- `newRenderSize`: The Picture in Picture content’s rendered size, in pixels.

## See Also

### Responding to playback events
- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](./pictureinpicturecontroller%28_,setplaying%29.md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerTimeRangeForPlayback(AVPictureInPictureController) -> CMTimeRange](./pictureinpicturecontrollertimerangeforplayback%28_%29.md)
  Asks the delegate for the current playable time range.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollerisplaybackpaused%28_%29.md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](./pictureinpicturecontroller%28_,skipbyinterval,completion%29.md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollershouldprohibitbackgroundaudioplayback%28_%29.md)
  Asks the delegate whether to always prohibit background audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:))*