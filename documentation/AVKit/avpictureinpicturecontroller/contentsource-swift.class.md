# AVPictureInPictureController.ContentSource

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVPictureInPictureControllerContentSource : NSObject
```

## Mentions

- [Adopting Picture in Picture for video calls](../adopting-picture-in-picture-for-video-calls.md)

## Overview

The system supports displaying content from an [`AVPlayerLayer`](../../AVFoundation/avplayerlayer.md) or [`AVSampleBufferDisplayLayer`](../../AVFoundation/avsamplebufferdisplaylayer.md) in a Picture in Picture window. Use an instance of this class to describe the source of your app’s content.

## Topics

### Creating a content source
- [init(playerLayer: AVPlayerLayer)](./contentsource-swift.class/init%28playerlayer%29.md)
  Creates a content source with a player layer.
- [init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)](./contentsource-swift.class/init%28samplebufferdisplaylayer,playbackdelegate%29.md)
  Creates a content source with a sample buffer display layer.
- [init(activeVideoCallSourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)](./contentsource-swift.class/init%28activevideocallsourceview,contentviewcontroller%29.md)
  Creates a content source with an active video call.
### Accessing the presentation layer
- [var playerLayer: AVPlayerLayer?](./contentsource-swift.class/playerlayer.md)
  The presenting player layer.
- [var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer?](./contentsource-swift.class/samplebufferdisplaylayer.md)
  The presenting sample buffer display layer.
### Accessing the active call presentation
- [var activeVideoCallSourceView: UIView?](./contentsource-swift.class/activevideocallsourceview.md)
  The view that contains the video content of the call.
- [var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController](./contentsource-swift.class/activevideocallcontentviewcontroller.md)
  The view controller that presents the video call content.
- [class AVPictureInPictureVideoCallViewController](../avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
### Configuring the delegate
- [var sampleBufferPlaybackDelegate: (any AVPictureInPictureSampleBufferPlaybackDelegate)?](./contentsource-swift.class/samplebufferplaybackdelegate.md)
  A delegate object that responds to sample buffer playback events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
### Invalidating state
- [func invalidatePlaybackState()](./invalidateplaybackstate%28%29.md)
  Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the content source
- [var contentSource: AVPictureInPictureController.ContentSource?](./contentsource-swift.property.md)
  The source of the controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class)*