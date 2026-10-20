# AVCaptureDevice.LensStabilizationStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
enum LensStabilizationStatus
```

```c
enum AVCaptureLensStabilizationStatus : NSInteger;
```

## Topics

### Lens stabilization values
- [AVCaptureDevice.LensStabilizationStatus.unsupported](./lensstabilizationstatus/unsupported.md)
  Lens stabilization isn’t available on the device or device configuration that captured this photo.
- [AVCaptureDevice.LensStabilizationStatus.off](./lensstabilizationstatus/off.md)
  Lens stabilization isn’t specified for this photo capture.
- [AVCaptureDevice.LensStabilizationStatus.active](./lensstabilizationstatus/active.md)
  Lens stabilization was active for the full duration of the photo capture.
- [AVCaptureDevice.LensStabilizationStatus.outOfRange](./lensstabilizationstatus/outofrange.md)
  Lens stabilization was enabled for the photo capture, but device motion or capture duration exceeded the stabilization module’s correction limits.
- [AVCaptureDevice.LensStabilizationStatus.unavailable](./lensstabilizationstatus/unavailable.md)
  Lens stabilization was temporarily unavailable during the photo capture.
### Initializers
- [init?(rawValue: Int)](./lensstabilizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensstabilizationstatus)*