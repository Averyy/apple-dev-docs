# continuityCamera

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A Continuity Camera device type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
static let continuityCamera: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeContinuityCamera;
```

#### Discussion

You discover devices of this type using an [`AVCaptureDevice.DiscoverySession`](../discoverysession.md) of by calling the device’s [`default(_:for:position:)`](../default%28_,for,position%29.md) method.

## See Also

### Cameras
- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](./builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInUltraWideCamera: AVCaptureDevice.DeviceType](./builtinultrawidecamera.md)
  A built-in camera device type with a shorter focal length than a wide-angle camera.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](./builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualCamera: AVCaptureDevice.DeviceType](./builtindualcamera.md)
  A built-in camera device type that consists of a wide-angle and telephoto camera.
- [static let builtInDualWideCamera: AVCaptureDevice.DeviceType](./builtindualwidecamera.md)
  A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](./builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](./builtinduocamera.md)
  A built-in dual camera device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/continuitycamera)*