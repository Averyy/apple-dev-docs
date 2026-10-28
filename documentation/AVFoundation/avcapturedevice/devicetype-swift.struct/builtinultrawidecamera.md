# builtInUltraWideCamera

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A built-in camera device type with a shorter focal length than a wide-angle camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
static let builtInUltraWideCamera: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeBuiltInUltraWideCamera;
```

## Discussion

You can only discover this device type using an [`AVCaptureDevice.DiscoverySession`](../discoverysession.md).

## See Also

### Cameras
- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](./builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](./builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualCamera: AVCaptureDevice.DeviceType](./builtindualcamera.md)
  A built-in camera device type that consists of a wide-angle and telephoto camera.
- [static let builtInDualWideCamera: AVCaptureDevice.DeviceType](./builtindualwidecamera.md)
  A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](./builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let continuityCamera: AVCaptureDevice.DeviceType](./continuitycamera.md)
  A Continuity Camera device type.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](./builtinduocamera.md)
  A built-in dual camera device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinultrawidecamera)*