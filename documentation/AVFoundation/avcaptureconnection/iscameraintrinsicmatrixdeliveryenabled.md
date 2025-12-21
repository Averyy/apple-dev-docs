# isCameraIntrinsicMatrixDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

You can set this property to [`true`](https://developer.apple.com/documentation/Swift/true) for a video connection if [`isCameraIntrinsicMatrixDeliverySupported`](avcaptureconnection/iscameraintrinsicmatrixdeliverysupported.md) is [`true`](https://developer.apple.com/documentation/Swift/true), and only before calling the [`AVCaptureSession`](avcapturesession.md) [`startRunning()`](avcapturesession/startrunning().md) method. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

Camera intrinsics describe the current imaging parameters of a capture device in ways that you can use to render overlays or perform computer vision tasks. If [`true`](https://developer.apple.com/documentation/Swift/true), any [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) instance in this connection can include the [`kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix`](https://developer.apple.com/documentation/CoreMedia/kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix) attachment for each sample buffer it vends.

## See Also

- [var isCameraIntrinsicMatrixDeliverySupported: Bool](avcaptureconnection/iscameraintrinsicmatrixdeliverysupported.md)
  A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled)*