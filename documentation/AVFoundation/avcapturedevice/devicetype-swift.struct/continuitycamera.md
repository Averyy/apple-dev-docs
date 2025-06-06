# continuityCamera

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

You discover devices of this type using an [`AVCaptureDevice.DiscoverySession`](avcapturedevice/discoverysession.md) of by calling the device’s [`default(_:for:position:)`](avcapturedevice/default(_:for:position:).md) method.

## See Also

- [static let builtInWideAngleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinwideanglecamera.md)
  A built-in wide-angle camera device type.
- [static let builtInUltraWideCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinultrawidecamera.md)
  A built-in camera device type with a shorter focal length than a wide-angle camera.
- [static let builtInTelephotoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintelephotocamera.md)
  A built-in camera device type with a longer focal length than a wide-angle camera.
- [static let builtInDualCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtindualcamera.md)
  A built-in camera device type that consists of a wide-angle and telephoto camera.
- [static let builtInDualWideCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtindualwidecamera.md)
  A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [static let builtInTripleCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtintriplecamera.md)
  A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [static let builtInDuoCamera: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct/builtinduocamera.md)
  A built-in dual camera device type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/continuitycamera)*