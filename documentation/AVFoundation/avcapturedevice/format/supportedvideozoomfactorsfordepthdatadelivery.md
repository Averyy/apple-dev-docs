# supportedVideoZoomFactorsForDepthDataDelivery

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The zoom factors that a format supports for depth data delivery.

**Availability**:
- iOS 16.0+ - Deprecated in 17.2
- iPadOS 16.0+ - Deprecated in 17.2
- Mac Catalyst 16.0+ - Deprecated in 17.2
- tvOS 17.0+ - Deprecated in 17.2

> **Deprecated**: Use AVCaptureDevice.Format.supportedVideoZoomRangesForDepthDataDelivery instead

## Declaration

```swift
@nonobjc
var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat] { get }
```

## See Also

### Determining depth capture support
- [var supportedDepthDataFormats: [AVCaptureDevice.Format]](./supporteddepthdataformats.md)
  The list of data formats compatible with this video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supportedvideozoomfactorsfordepthdatadelivery)*