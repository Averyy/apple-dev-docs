# maxAvailableVideoZoomFactor

**Framework**: AVFoundation  
**Kind**: property

The maximum zoom factor allowed in the current capture configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var maxAvailableVideoZoomFactor: CGFloat { get }
```

#### Discussion

On single-camera devices, this value is always equal to the device format’s [`videoMaxZoomFactor`](avcapturedevice/format/videomaxzoomfactor.md) value. On a dual-camera device, the allowed range of video zoom factors can change if the device is delivering depth data to one or more capture outputs.

Setting the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property to (or calling the [`ramp(toVideoZoomFactor:withRate:)`](avcapturedevice/ramp(tovideozoomfactor:withrate:).md) method with) a value greater than the device format’s [`videoMaxZoomFactor`](avcapturedevice/format/videomaxzoomfactor.md) value always raises an exception. Setting the video zoom factor to a value between the maximum available zoom factor and the device format’s maximum clamps the zoom setting to the maximum available value.

This property is key-value observable.

## See Also

- [var minAvailableVideoZoomFactor: CGFloat](avcapturedevice/minavailablevideozoomfactor.md)
  The minimum zoom factor allowed in the current capture configuration.
- [var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber]](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md)
  An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [var dualCameraSwitchOverVideoZoomFactor: CGFloat](avcapturedevice/dualcameraswitchovervideozoomfactor.md)
  The video zoom factor at which a dual camera device can automatically switch between cameras.
- [var displayVideoZoomFactorMultiplier: CGFloat](avcapturedevice/displayvideozoomfactormultiplier.md)
  A video zoom factor multiplier to use when displaying zoom information in a user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxavailablevideozoomfactor)*