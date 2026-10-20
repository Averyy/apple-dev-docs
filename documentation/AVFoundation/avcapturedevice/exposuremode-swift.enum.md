# AVCaptureDevice.ExposureMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureExposureMode : NSInteger;
```

## Topics

### Exposure modes
- [AVCaptureDevice.ExposureMode.locked](./exposuremode-swift.enum/locked.md)
  A mode that locks exposure for the device.
- [AVCaptureDevice.ExposureMode.autoExpose](./exposuremode-swift.enum/autoexpose.md)
  A mode that automatically adjusts the exposure one time, and then locks exposure for the device.
- [AVCaptureDevice.ExposureMode.continuousAutoExposure](./exposuremode-swift.enum/continuousautoexposure.md)
  A mode that continuously monitors exposure levels and automatically adjusts exposure when necessary.
- [AVCaptureDevice.ExposureMode.custom](./exposuremode-swift.enum/custom.md)
  A mode where an app manually sets the exposure duration and ISO values.
### Initializers
- [init?(rawValue: Int)](./exposuremode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the exposure mode
- [func isExposureModeSupported(AVCaptureDevice.ExposureMode) -> Bool](./isexposuremodesupported%28_%29.md)
  Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [var exposureMode: AVCaptureDevice.ExposureMode](./exposuremode-swift.property.md)
  The exposure mode for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.enum)*