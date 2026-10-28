# videoMaxZoomFactorForDepthDataDelivery

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A maximum zoom factor the device supports when configured for depth data delivery.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0

> **Deprecated**: Use [`supportedVideoZoomFactorsForDepthDataDelivery`](../../avcapturedeviceformat/supportedvideozoomfactorsfordepthdatadelivery.md) instead.

## Declaration

```swift
var videoMaxZoomFactorForDepthDataDelivery: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat videoMaxZoomFactorForDepthDataDelivery;
```

## Discussion

Depth data capture requires coordinating the zoom factors of the two cameras on a dual-camera device. Therefore, when you enable depth data delivery for a capture format using the [`AVCaptureDepthDataOutput`](../../avcapturedepthdataoutput.md) class, the range of available values for the device’s [`videoZoomFactor`](../videozoomfactor.md) property is reduced.

If this format doesn’t support depth capture, this property’s value is the same as that of the [`videoMaxZoomFactor`](./videomaxzoomfactor.md) property.

## See Also

### Determining zoom capabilities
- [var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat]](./supportedvideozoomfactorsfordepthdatadelivery.md)
  The zoom factors that a format supports for depth data delivery.
- [var videoMinZoomFactorForDepthDataDelivery: CGFloat](./videominzoomfactorfordepthdatadelivery.md)
  A minimum zoom factor the device supports when configured for depth data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactorfordepthdatadelivery)*