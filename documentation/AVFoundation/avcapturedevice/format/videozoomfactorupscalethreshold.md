# videoZoomFactorUpscaleThreshold

**Framework**: AVFoundation  
**Kind**: property

A threshold at which the system upscales pixel data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoZoomFactorUpscaleThreshold: CGFloat { get }
```

#### Discussion

The device achieves a zoom effect by cropping around the center of the image captured by the sensor. At low zoom factors, the cropped images is equal to or larger than the output size. At higher zoom factors, the device must scale the cropped image up to the output size, resulting in a loss of image quality. This property indicates the factors at which upscaling occurs.

## See Also

- [var systemRecommendedVideoZoomRange: ClosedRange<CGFloat>?](avcapturedevice/format/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var secondaryNativeResolutionZoomFactors: [CGFloat]](avcapturedevice/format/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>]](avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videozoomfactorupscalethreshold)*