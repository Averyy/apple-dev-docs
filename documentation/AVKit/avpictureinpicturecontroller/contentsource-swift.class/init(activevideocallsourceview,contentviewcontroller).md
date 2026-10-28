# init(activeVideoCallSourceView:contentViewController:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

Creates a content source with an active video call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
init(activeVideoCallSourceView sourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)
```

```objc
- (instancetype) initWithActiveVideoCallSourceView:(UIView *) sourceView contentViewController:(AVPictureInPictureVideoCallViewController *) contentViewController;
```

## Discussion

The instance is only valid for the duration of the call.

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](../../../AVFoundation/avcapturesession/ismultitaskingcameraaccessenabled.md) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](../../../BundleResources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement to use the camera in PiP mode.

## Parameters

- `sourceView`: A view that contains the content of the video call.
- `contentViewController`: The view controller to appear in the system’s Picture in Picture window.

## See Also

### Creating a content source
- [init(playerLayer: AVPlayerLayer)](./init%28playerlayer%29.md)
  Creates a content source with a player layer.
- [init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)](./init%28samplebufferdisplaylayer,playbackdelegate%29.md)
  Creates a content source with a sample buffer display layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:))*