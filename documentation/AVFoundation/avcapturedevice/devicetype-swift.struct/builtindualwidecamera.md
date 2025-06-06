# builtInDualWideCamera

**Framework**: AVFoundation  
**Kind**: property

A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
static let builtInDualWideCamera: AVCaptureDevice.DeviceType
```

#### Discussion

The built-in dual camera supports the following features:

- Automatic switching from one camera to another when zoom factor, light level, and focus position allow.
- Generating depth data by measuring the disparities between the images captured by the ultrawide and wide-angle cameras.
- Delivery of photos from constituent ultrawide and wide-angle devices through a single photo capture request.

The built-in dual camera doesn’t support the following features:

- [`AVCaptureDevice.ExposureMode.custom`](avcapturedevice/exposuremode-swift.enum/custom.md) and manual exposure bracketing.
- Locking focus with a lens position other than [`currentLensPosition`](avcapturedevice/currentlensposition.md).
- Locking automatic white balance with device white balance gains other than [`currentWhiteBalanceGains`](avcapturedevice/currentwhitebalancegains.md).

Even when locked, exposure duration, ISO, aperture, white balance gains, or lens position may change when the device switches from one camera to another. However, the overall exposure, white balance, and focus position should be consistent.

> **Note**:  You can only discover this device type using an [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md) or the [`AVCaptureDevice`](avcapturedevice.md) [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md) method.

 You can only discover this device type using an [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md) or the [`AVCaptureDevice`](avcapturedevice.md) [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md) method.

## See Also

- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInUltraWideCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinultrawidecamera.md)
  A built-in camera device type with a shorter focal length than a wide-angle camera.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtindualcamera.md)
  A built-in camera device type that consists of a wide-angle and telephoto camera.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let continuityCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/continuitycamera.md)
  A Continuity Camera device type.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinduocamera.md)
  A built-in dual camera device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtindualwidecamera)*