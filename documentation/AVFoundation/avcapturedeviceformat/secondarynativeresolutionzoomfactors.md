# secondaryNativeResolutionZoomFactors

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The zoom factors at which this device transitions to secondary native resolution modes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * secondaryNativeResolutionZoomFactors;
```

#### Discussion

Devices that provide secondary native resolution zoom factors can switch their pixel sampling mode dynamically to produce high-fidelity images without upscaling at a fixed zoom factor beyond 1.0.

## See Also

### Determining zoom capabilities
- [systemRecommendedVideoZoomRange](./systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](../avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](../avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [supportedVideoZoomRangesForDepthDataDelivery](./supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [AVZoomRange](../avzoomrange.md)
  An object that defines an inclusive range of zoom values.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](../avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/secondarynativeresolutionzoomfactors)*