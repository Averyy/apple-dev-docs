# AVPictureInPictureController

**Framework**: AVKit  
**Kind**: class

A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class AVPictureInPictureController
```

## Mentions

- [Adopting Picture in Picture in a custom player](adopting-picture-in-picture-in-a-custom-player.md)
- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Overview

To use Picture in Picture, you need to configure your app to support background audio playback. See [`Configuring your app for media playback`](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) for more details.

Before presenting a user interface to start Picture in Picture, call the [`isPictureInPictureSupported()`](avpictureinpicturecontroller/ispictureinpicturesupported().md) method to determine if the current device supports the feature, and check the [`isPictureInPicturePossible`](avpictureinpicturecontroller/ispictureinpicturepossible.md) property value to determine whether PiP is possible in the current context.

> ❗ **Important**:  The framework doesn’t support subclassing [`AVPictureInPictureController`](avpictureinpicturecontroller.md).

## Topics

### Creating a controller
- [init(contentSource: AVPictureInPictureController.ContentSource)](avpictureinpicturecontroller/init(contentsource:).md)
  Creates a Picture in Picture controller with a content source.
- [convenience init?(playerLayer: AVPlayerLayer)](avpictureinpicturecontroller/init(playerlayer:).md)
  Creates a Picture in Picture controller with a player layer.
### Configuring the content source
- [var contentSource: AVPictureInPictureController.ContentSource?](avpictureinpicturecontroller/contentsource-swift.property.md)
  The source of the controller’s content.
- [AVPictureInPictureController.ContentSource](avpictureinpicturecontroller/contentsource-swift.class.md)
  An object that represents the source of the content to present in Picture in Picture.
### Accessing the player layer
- [var playerLayer: AVPlayerLayer](avpictureinpicturecontroller/playerlayer.md)
  The layer that displays the video content.
### Configuring playback behavior
- [var requiresLinearPlayback: Bool](avpictureinpicturecontroller/requireslinearplayback.md)
  A Boolean value that determines whether the controller allows the user to skip media content.
### Accessing the delegate object
- [var delegate: (any AVPictureInPictureControllerDelegate)?](avpictureinpicturecontroller/delegate.md)
  A delegate object for a Picture in Picture controller.
- [protocol AVPictureInPictureControllerDelegate](avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
### Accessing Picture in Picture state
- [class func isPictureInPictureSupported() -> Bool](avpictureinpicturecontroller/ispictureinpicturesupported.md)
  Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [var isPictureInPicturePossible: Bool](avpictureinpicturecontroller/ispictureinpicturepossible.md)
  A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [var isPictureInPictureActive: Bool](avpictureinpicturecontroller/ispictureinpictureactive.md)
  A Boolean value that indicates whether the Picture in Picture window is onscreen.
- [var isPictureInPictureSuspended: Bool](avpictureinpicturecontroller/ispictureinpicturesuspended.md)
  A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.
### Controlling Picture in Picture playback
- [var canStopPictureInPicture: Bool](avpictureinpicturecontroller/canstoppictureinpicture.md)
  A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [var canStartPictureInPictureAutomaticallyFromInline: Bool](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md)
  A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [func startPictureInPicture()](avpictureinpicturecontroller/startpictureinpicture.md)
  Starts Picture in Picture, if possible.
- [func stopPictureInPicture()](avpictureinpicturecontroller/stoppictureinpicture.md)
  Stops Picture in Picture, if active.
- [func invalidatePlaybackState()](avpictureinpicturecontroller/invalidateplaybackstate.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.
### Retrieving Picture in Picture template images
- [class var pictureInPictureButtonStartImage: UIImage](avpictureinpicturecontroller/pictureinpicturebuttonstartimage.md)
  A system-default template image for the button that starts Picture in Picture in your app.
- [class var pictureInPictureButtonStopImage: UIImage](avpictureinpicturecontroller/pictureinpicturebuttonstopimage.md)
  A system-default template image for the button that stops Picture in Picture in your app.
- [class func pictureInPictureButtonStartImage(compatibleWith: UITraitCollection?) -> UIImage](avpictureinpicturecontroller/pictureinpicturebuttonstartimage(compatiblewith:).md)
  Returns a system-default template image that’s compatible with a trait collection for the button that starts Picture in Picture in your app.
- [class func pictureInPictureButtonStopImage(compatibleWith: UITraitCollection?) -> UIImage](avpictureinpicturecontroller/pictureinpicturebuttonstopimage(compatiblewith:).md)
  Returns a system-default template image that’s compatible with a trait collection for the button that stops Picture in Picture in your app.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Adopting Picture in Picture in a standard player](adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a custom player](adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)
  Add multitasking capability to your video-call apps by using Picture in Picture (PiP).
- [Adopting Picture in Picture playback in tvOS](adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [protocol AVPictureInPictureControllerDelegate](avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
- [class AVPictureInPictureVideoCallViewController](avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
- [protocol AVPlayerViewPictureInPictureDelegate](avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller)*