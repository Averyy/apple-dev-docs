# pictureInPictureController(_:skipByInterval:completion:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime, completion completionHandler: @escaping @Sendable () -> Void)
```

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime) async
```

```objc
- (void) pictureInPictureController:(AVPictureInPictureController *) pictureInPictureController skipByInterval:(CMTime) skipInterval completionHandler:(void (^)()) completionHandler;
```

#### Discussion

Your app’s implementation of this method may choose to seek by a different interval for efficiency reasons, such as seeking to a particular key frame or only allowing seeks that fall within the playable timeline.

> ❗ **Important**:  Before calling the completion handler, ensure the seek operation is complete and the timebase reflects the current time and playback rate.

## Parameters

- `pictureInPictureController`: The Picture in Picture controller.
- `skipInterval`: A [`CMTime`](../../CoreMedia/cmtime.md) value that indicates the time interval by which to skip.
- `completionHandler`: You must call the completion handler whether your seek operation succeeds or fails. Failing to call the completion handler is an app error and leaves the user interface in a seeking state.

## See Also

### Responding to playback events
- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](./pictureinpicturecontroller%28_,setplaying%29.md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerTimeRangeForPlayback(AVPictureInPictureController) -> CMTimeRange](./pictureinpicturecontrollertimerangeforplayback%28_%29.md)
  Asks the delegate for the current playable time range.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollerisplaybackpaused%28_%29.md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](./pictureinpicturecontroller%28_,didtransitiontorendersize%29.md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](./pictureinpicturecontrollershouldprohibitbackgroundaudioplayback%28_%29.md)
  Asks the delegate whether to always prohibit background audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:))*