# supportedVideoZoomRangesForDepthDataDelivery

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The zoom ranges that support the delivery of depth data.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<AVZoomRange *> * supportedVideoZoomRangesForDepthDataDelivery;
```

## Discussion

Virtual devices support limited zoom ranges when delivering depth data to any output. If a device format has no [`supportedDepthDataFormats`](../avcapturedevice/format/supporteddepthdataformats.md) values, this property value is an empty array.

The presence of one or more ranges where the minimum and maximum zoom factors aren’t equal means the system supports continuous zoom with depth. For example, if the value of this property contains zoom ranges with equal minimum and maximum values, the system only allows you to set zoom factors equal to these values when you enable depth data delivery. Setting a zoom factor other than these values results in an exception. Alternatively, when a range’s minimum and maximum values aren’t the same, the system supports depth data delivery with across a range of zoom factors. You can set a zoom factor outside this range, but results in a loss of depth data. Setting the zoom factor back to the supported range resumes depth data delivery.

When you enable depth data delivery, the effective [`videoZoomFactorUpscaleThreshold`](../avcapturedevice/format/videozoomfactorupscalethreshold.md) is `1.0`, which means that all zoom factors that aren’t native zoom factors (see [`virtualDeviceSwitchOverVideoZoomFactors`](../avcapturedevice/virtualdeviceswitchovervideozoomfactors.md) and [`secondaryNativeResolutionZoomFactors`](../avcapturedevice/format/secondarynativeresolutionzoomfactors.md)) result in digital upscaling.

## See Also

### Determining zoom capabilities
- [systemRecommendedVideoZoomRange](./systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](../avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](../avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](./secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [AVZoomRange](../avzoomrange.md)
  An object that defines an inclusive range of zoom values.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](../avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/supportedvideozoomrangesfordepthdatadelivery)*