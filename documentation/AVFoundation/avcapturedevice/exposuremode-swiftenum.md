# AVCaptureDevice.ExposureMode

**Framework**: AVFoundation  
**Kind**: enum

Constants that specify the exposure mode of a capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
enum ExposureMode
```

## Topics

### Exposure modes
- [AVCaptureDevice.ExposureMode.locked](avcapturedevice/exposuremode-swift.enum/locked.md)
  A mode that locks exposure for the device.
- [AVCaptureDevice.ExposureMode.autoExpose](avcapturedevice/exposuremode-swift.enum/autoexpose.md)
  A mode that automatically adjusts the exposure one time, and then locks exposure for the device.
- [AVCaptureDevice.ExposureMode.continuousAutoExposure](avcapturedevice/exposuremode-swift.enum/continuousautoexposure.md)
  A mode that continuously monitors exposure levels and automatically adjusts exposure when necessary.
- [AVCaptureDevice.ExposureMode.custom](avcapturedevice/exposuremode-swift.enum/custom.md)
  A mode where an app manually sets the exposure duration and ISO values.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/exposuremode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isExposureModeSupported(AVCaptureDevice.ExposureMode) -> Bool](avcapturedevice/isexposuremodesupported(_:).md)
  Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [var exposureMode: AVCaptureDevice.ExposureMode](avcapturedevice/exposuremode-swift.property.md)
  The exposure mode for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.enum)*