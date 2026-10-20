# isCameraIntrinsicMatrixDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isCameraIntrinsicMatrixDeliveryEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isCameraIntrinsicMatrixDeliveryEnabled) BOOL cameraIntrinsicMatrixDeliveryEnabled;
```

#### Discussion

You can set this property to [`true`](../../Swift/true.md) for a video connection if [`isCameraIntrinsicMatrixDeliverySupported`](./iscameraintrinsicmatrixdeliverysupported.md) is [`true`](../../Swift/true.md), and only before calling the [`AVCaptureSession`](../avcapturesession.md) [`startRunning()`](../avcapturesession/startrunning%28%29.md) method. The default value is [`false`](../../Swift/false.md).

Camera intrinsics describe the current imaging parameters of a capture device in ways that you can use to render overlays or perform computer vision tasks. If [`true`](../../Swift/true.md), any [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) instance in this connection can include the [`kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix`](../../CoreMedia/kcmsamplebufferattachmentkey_cameraintrinsicmatrix.md) attachment for each sample buffer it vends.

## See Also

### Delivering camera calibration settings
- [var isCameraIntrinsicMatrixDeliverySupported: Bool](./iscameraintrinsicmatrixdeliverysupported.md)
  A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled)*