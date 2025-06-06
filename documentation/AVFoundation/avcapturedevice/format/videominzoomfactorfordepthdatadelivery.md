# videoMinZoomFactorForDepthDataDelivery

**Framework**: AVFoundation  
**Kind**: property

A minimum zoom factor the device supports when configured for depth data delivery.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var videoMinZoomFactorForDepthDataDelivery: CGFloat { get }
```

#### Discussion

Depth data capture requires coordinating the zoom factors of the two cameras on a dual-camera device. Therefore, when you enable depth data delivery for a capture format using the [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) class, the range of available values for the device’s [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property is reduced.

If this format doesn’t support depth capture, this property’s value is `1.0`.

## See Also

- [var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat]](avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery.md)
  The zoom factors that a format supports for depth data delivery.
- [var videoMaxZoomFactorForDepthDataDelivery: CGFloat](avcapturedevice/format/videomaxzoomfactorfordepthdatadelivery.md)
  A maximum zoom factor the device supports when configured for depth data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videominzoomfactorfordepthdatadelivery)*