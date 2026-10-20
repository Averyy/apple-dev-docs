# AVPictureInPictureSampleBufferPlaybackDelegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for controlling playback from a sample buffer display layer in Picture in Picture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVPictureInPictureSampleBufferPlaybackDelegate : NSObjectProtocol
```

```objc
@protocol AVPictureInPictureSampleBufferPlaybackDelegate <NSObject>
```

## Topics

### Responding to playback events
- [func pictureInPictureController(AVPictureInPictureController, setPlaying: Bool)](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_,setplaying%29.md)
  Tells the delegate that the user requested to begin or pause playback.
- [func pictureInPictureControllerTimeRangeForPlayback(AVPictureInPictureController) -> CMTimeRange](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback%28_%29.md)
  Asks the delegate for the current playable time range.
- [func pictureInPictureControllerIsPlaybackPaused(AVPictureInPictureController) -> Bool](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused%28_%29.md)
  Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [func pictureInPictureController(AVPictureInPictureController, didTransitionToRenderSize: CMVideoDimensions)](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_,didtransitiontorendersize%29.md)
  Tells the delegate when the system Picture in Picture window changes size.
- [func pictureInPictureController(AVPictureInPictureController, skipByInterval: CMTime, completion: () -> Void)](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_,skipbyinterval,completion%29.md)
  Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(AVPictureInPictureController) -> Bool](./avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback%28_%29.md)
  Asks the delegate whether to always prohibit background audio playback.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Picture in Picture
- [Adopting Picture in Picture in a standard player](./adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a custom player](./adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](./adopting-picture-in-picture-for-video-calls.md)
  Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Adopting Picture in Picture playback in tvOS](./adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [class AVPictureInPictureController](./avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.
- [protocol AVPictureInPictureControllerDelegate](./avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
- [class AVPictureInPictureVideoCallViewController](./avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
- [protocol AVPlayerViewPictureInPictureDelegate](./avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate)*