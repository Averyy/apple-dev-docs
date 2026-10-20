# videoMaxZoomFactor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A maximum zoom factor the format allows.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoMaxZoomFactor: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat videoMaxZoomFactor;
```

#### Discussion

A maximum factor of `1.0` indicates that the format isn’t capable of zooming.

## See Also

### Determining zoom capabilities
- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](./systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoZoomFactorUpscaleThreshold: CGFloat](./videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](./secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](./supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](./zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactor)*