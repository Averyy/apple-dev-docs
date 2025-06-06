# zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+

## Declaration

```swift
var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool { get }
```

#### Discussion

Setting a zoom factor outside the range defined by the [`supportedVideoZoomFactorsForDepthDataDelivery`](avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery.md) property results in the system suspending depth data delivery. It resumes delivery when you set the zoom factor back to a supported value.

## See Also

- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](avcapturedevice/format/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](avcapturedevice/format/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported)*