# AVCaptureDevice.CenterStageControlMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the current Center Stage control mode.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
enum CenterStageControlMode
```

```c
enum AVCaptureCenterStageControlMode : NSInteger;
```

## Topics

### Control modes
- [AVCaptureDevice.CenterStageControlMode.user](./centerstagecontrolmode-swift.enum/user.md)
  The user controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.app](./centerstagecontrolmode-swift.enum/app.md)
  The app controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.cooperative](./centerstagecontrolmode-swift.enum/cooperative.md)
  A user and app cooperatively share control of Center Stage.
### Initializers
- [init?(rawValue: Int)](./centerstagecontrolmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring Center Stage
- [var isCenterStageActive: Bool](./iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](./iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](./centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](./centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.
- [centerStageRectOfInterestSupported](./centerstagerectofinterestsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum)*