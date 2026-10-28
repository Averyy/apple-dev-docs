# systemRecommendedVideoZoomRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The system’s recommended zoom range for this device format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) AVZoomRange * systemRecommendedVideoZoomRange;
```

## Discussion

Use this value to create a slider in your app’s user interface that controls a device’s zoom within a system-recommended range. When a recommendation isn’t available, this property returns `nil`.

Apps can key-value observe a capture device’s [`minAvailableVideoZoomFactor`](../avcapturedevice/minavailablevideozoomfactor.md) and [`maxAvailableVideoZoomFactor`](../avcapturedevice/maxavailablevideozoomfactor.md) property values to know when a device limits its supported zoom to the recommended range.

> **Note**:  The framework uses this value to define the range of an [`AVCaptureSystemZoomSlider`](../avcapturesystemzoomslider.md) control.

## See Also

### Determining zoom capabilities
- [var videoMaxZoomFactor: CGFloat](../avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](../avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](./secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](./supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [AVZoomRange](../avzoomrange.md)
  An object that defines an inclusive range of zoom values.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](../avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/systemrecommendedvideozoomrange)*