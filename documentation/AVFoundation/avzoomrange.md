# AVZoomRange

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that defines an inclusive range of zoom values.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+

## Declaration

```objc
@interface AVZoomRange : NSObject
```

## Topics

### Inspecting a range
- [minZoomFactor](./avzoomrange/minzoomfactor.md)
  The range’s minimum zoom factor.
- [maxZoomFactor](./avzoomrange/maxzoomfactor.md)
  The range’s maximum zoom factor.
- [- containsZoomFactor:](./avzoomrange/containszoomfactor_.md)
  Returns a Boolean value that indicates whether the specified zoom factor exists in the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Determining zoom capabilities
- [systemRecommendedVideoZoomRange](./avcapturedeviceformat/systemrecommendedvideozoomrange.md)
  The system’s recommended zoom range for this device format.
- [var videoMaxZoomFactor: CGFloat](./avcapturedevice/format/videomaxzoomfactor.md)
  A maximum zoom factor the format allows.
- [var videoZoomFactorUpscaleThreshold: CGFloat](./avcapturedevice/format/videozoomfactorupscalethreshold.md)
  A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](./avcapturedeviceformat/secondarynativeresolutionzoomfactors.md)
  The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](./avcapturedeviceformat/supportedvideozoomrangesfordepthdatadelivery.md)
  The zoom ranges that support the delivery of depth data.
- [var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool](./avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md)
  A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avzoomrange)*