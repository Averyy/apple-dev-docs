# videoZoomFactor

**Framework**: AVFoundation  
**Kind**: property

A value that controls the cropping and enlargement of images captured by the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoZoomFactor: CGFloat { get set }
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

This value is a multiplier. For example, a value of `2.0` doubles the size of an image’s subject (and halves the field of view). Allowed values range from `1.0` (full field of view) to the value of the active format’s [`videoMaxZoomFactor`](avcapturedevice/format/videomaxzoomfactor.md) property. Setting the value of this property jumps immediately to the new zoom factor. For a smooth transition, use the [`ramp(toVideoZoomFactor:withRate:)`](avcapturedevice/ramp(tovideozoomfactor:withrate:).md) method.

The device achieves a zoom effect by cropping around the center of the image captured by the sensor. At low zoom factors, the cropped images is equal to or larger than the output size. At higher zoom factors, the device must scale the cropped image up to the output size, resulting in a loss of image quality. The active format’s [`videoZoomFactorUpscaleThreshold`](avcapturedevice/format/videozoomfactorupscalethreshold.md) property indicates the factors at which upscaling occurs.

Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

## See Also

- [func ramp(toVideoZoomFactor: CGFloat, withRate: Float)](avcapturedevice/ramp(tovideozoomfactor:withrate:).md)
  Begins a smooth transition from the current zoom factor to another.
- [func cancelVideoZoomRamp()](avcapturedevice/cancelvideozoomramp.md)
  Smoothly ends a zoom transition in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/videozoomfactor)*