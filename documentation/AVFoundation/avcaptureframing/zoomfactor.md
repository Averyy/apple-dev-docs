# zoomFactor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A zoom factor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var zoomFactor: Float { get }
```

```objc
@property (atomic, readonly) float zoomFactor;
```

## Discussion

Suitable for use with the [`videoZoomFactor`](../avcapturedevice/videozoomfactor.md) property or [`ramp(toVideoZoomFactor:withRate:)`](../avcapturedevice/ramp%28tovideozoomfactor,withrate%29.md).

## See Also

### Inspecting a framing
- [var aspectRatio: AVCaptureDevice.AspectRatio](./aspectratio.md)
  An aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureframing/zoomfactor)*