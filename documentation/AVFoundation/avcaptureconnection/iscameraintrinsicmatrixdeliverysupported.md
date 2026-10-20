# isCameraIntrinsicMatrixDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isCameraIntrinsicMatrixDeliverySupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCameraIntrinsicMatrixDeliverySupported) BOOL cameraIntrinsicMatrixDeliverySupported;
```

#### Discussion

A value of [`true`](../../Swift/true.md) means you can set [`isCameraIntrinsicMatrixDeliveryEnabled`](./iscameraintrinsicmatrixdeliveryenabled.md) to [`true`](../../Swift/true.md). The property is only [`true`](../../Swift/true.md) if both the connection’s input device format and output type support delivering camera intrinsics. In iOS 11, the [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) class is the only output type that supports camera intrinsics.

## See Also

### Delivering camera calibration settings
- [var isCameraIntrinsicMatrixDeliveryEnabled: Bool](./iscameraintrinsicmatrixdeliveryenabled.md)
  A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliverysupported)*