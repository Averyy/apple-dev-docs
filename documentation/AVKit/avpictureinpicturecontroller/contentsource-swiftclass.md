# AVPictureInPictureController.ContentSource

**Framework**: AVKit  
**Kind**: class

An object that represents the source of the content to present in Picture in Picture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class ContentSource
```

## Mentions

- [Adopting Picture in Picture for video calls](adopting-picture-in-picture-for-video-calls.md)

#### Overview

The system supports displaying content from an [`AVPlayerLayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayerLayer) or [`AVSampleBufferDisplayLayer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferDisplayLayer) in a Picture in Picture window. Use an instance of this class to describe the source of your app’s content.

## Topics

### Creating a Content Source
- [init(playerLayer: AVPlayerLayer)](avpictureinpicturecontroller/contentsource-swift.class/init(playerlayer:).md)
  Creates a content source with a player layer.
- [init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)](avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:).md)
  Creates a content source with a sample buffer display layer.
- [init(activeVideoCallSourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)](avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:).md)
  Creates a content source with an active video call.
### Accessing the Presentation Layer
- [var playerLayer: AVPlayerLayer?](avpictureinpicturecontroller/contentsource-swift.class/playerlayer.md)
  The presenting player layer.
- [var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer?](avpictureinpicturecontroller/contentsource-swift.class/samplebufferdisplaylayer.md)
  The presenting sample buffer display layer.
### Accessing the Active Call Presentation
- [var activeVideoCallSourceView: UIView?](avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview.md)
  The view that contains the video content of the call.
- [var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController](avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller.md)
  The view controller that presents the video call content.
- [class AVPictureInPictureVideoCallViewController](avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
### Configuring the Delegate
- [var sampleBufferPlaybackDelegate: (any AVPictureInPictureSampleBufferPlaybackDelegate)?](avpictureinpicturecontroller/contentsource-swift.class/samplebufferplaybackdelegate.md)
  A delegate object that responds to sample buffer playback events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
### Invalidating State
- [func invalidatePlaybackState()](avpictureinpicturecontroller/invalidateplaybackstate.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var contentSource: AVPictureInPictureController.ContentSource?](avpictureinpicturecontroller/contentsource-swift.property.md)
  The source of the controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class)*