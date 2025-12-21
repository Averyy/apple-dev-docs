# isCameraIntrinsicMatrixDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

A value of [`true`](https://developer.apple.com/documentation/Swift/true) means you can set [`isCameraIntrinsicMatrixDeliveryEnabled`](avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled.md) to [`true`](https://developer.apple.com/documentation/Swift/true). The property is only [`true`](https://developer.apple.com/documentation/Swift/true) if both the connection’s input device format and output type support delivering camera intrinsics. In iOS 11, the [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) class is the only output type that supports camera intrinsics.

## See Also

- [var isCameraIntrinsicMatrixDeliveryEnabled: Bool](avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled.md)
  A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliverysupported)*