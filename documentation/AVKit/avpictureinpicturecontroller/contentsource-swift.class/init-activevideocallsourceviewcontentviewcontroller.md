# init(activeVideoCallSourceView:contentViewController:)

**Framework**: AVKit  
**Kind**: init

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

#### Discussion

The instance is only valid for the duration of the call.

> ❗ **Important**:  The use of this API requires an entitlement. For information about requesting access, see [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.avfoundation.multitasking-camera-access).

## Parameters

- `sourceView`: A view that contains the content of the video call.
- `contentViewController`: The view controller to appear in the system’s Picture in Picture window.

## See Also

- [init(playerLayer: AVPlayerLayer)](avpictureinpicturecontroller/contentsource-swift.class/init(playerlayer:).md)
  Creates a content source with a player layer.
- [init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)](avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:).md)
  Creates a content source with a sample buffer display layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:))*