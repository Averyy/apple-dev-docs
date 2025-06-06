# minAvailableVideoZoomFactor

**Framework**: AVFoundation  
**Kind**: property

The minimum zoom factor allowed in the current capture configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var minAvailableVideoZoomFactor: CGFloat { get }
```

#### Discussion

On single-camera devices, this value is always `1.0`. On a dual-camera device, the allowed range of video zoom factors can change if the device is delivering depth data to one or more capture outputs.

Setting the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property to (or calling the [`ramp(toVideoZoomFactor:withRate:)`](avcapturedevice/ramp(tovideozoomfactor:withrate:).md) method with) a value less than `1.0` always raises an exception. Setting the video zoom factor to a value between `1.0` and the minimum available zoom factor clamps the zoom setting to the minimum.

This property is key-value observable.

## See Also

- [var maxAvailableVideoZoomFactor: CGFloat](avcapturedevice/maxavailablevideozoomfactor.md)
  The maximum zoom factor allowed in the current capture configuration.
- [var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber]](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md)
  An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [var dualCameraSwitchOverVideoZoomFactor: CGFloat](avcapturedevice/dualcameraswitchovervideozoomfactor.md)
  The video zoom factor at which a dual camera device can automatically switch between cameras.
- [var displayVideoZoomFactorMultiplier: CGFloat](avcapturedevice/displayvideozoomfactormultiplier.md)
  A video zoom factor multiplier to use when displaying zoom information in a user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/minavailablevideozoomfactor)*