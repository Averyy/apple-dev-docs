# zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported;
```

## Discussion

Setting a zoom factor outside the range defined by the [`supportedVideoZoomFactorsForDepthDataDelivery`](./supportedvideozoomfactorsfordepthdatadelivery.md) property results in the system suspending depth data delivery. It resumes delivery when you set the zoom factor back to a supported value.

## See Also

### Determining zoom capabilities
- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](./systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](./videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](./videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](./secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](./supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [systemRecommendedVideoZoomRange](../../avcapturedeviceformat/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [secondaryNativeResolutionZoomFactors](../../avcapturedeviceformat/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](../../avcapturedeviceformat/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [AVZoomRange](../../avzoomrange.md)
  An object that defines an inclusive range of zoom values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported)*