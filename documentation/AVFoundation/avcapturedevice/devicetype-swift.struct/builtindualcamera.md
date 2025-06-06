# builtInDualCamera

**Framework**: AVFoundation  
**Kind**: property

A built-in camera device type that consists of a wide-angle and telephoto camera.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
static let builtInDualCamera: AVCaptureDevice.DeviceType
```

## Mentions

- [Capturing Photos with Depth](capturing-photos-with-depth.md)

#### Discussion

This device type supports the following features:

- Automatic switching from one camera to the other when the zoom factor, light level, and focus position allow.
- Higher-quality zoom for still captures by fusing images from both cameras.
- Depth data delivery by measuring the disparity of matched features between the wide and telephoto cameras.
- Delivery of photos from constituent devices (wide and telephoto cameras) from a single photo capture request.

It doesn’t support the features below:

- Setting a [`AVCaptureDevice.ExposureMode.custom`](avcapturedevice/exposuremode-swift.enum/custom.md) exposure mode or manual exposure bracketing.
- Locking focus with a lens position to a value other than [`currentLensPosition`](avcapturedevice/currentlensposition.md).
- Locking automatic white balance with device white balance gains other than [`currentWhiteBalanceGains`](avcapturedevice/currentwhitebalancegains.md).

Even when locked, exposure duration, ISO, aperture, white balance gains, or lens position may change when the device switches from one camera to the other. The overall exposure, white balance, and focus position however should be consistent.

You can only retrieve devices of this type using an [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md) or by calling [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md).

## See Also

- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInUltraWideCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinultrawidecamera.md)
  A built-in camera device type with a shorter focal length than a wide-angle camera.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualWideCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtindualwidecamera.md)
  A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let continuityCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/continuitycamera.md)
  A Continuity Camera device type.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinduocamera.md)
  A built-in dual camera device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtindualcamera)*