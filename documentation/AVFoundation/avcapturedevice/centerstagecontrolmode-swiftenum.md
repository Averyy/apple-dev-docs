# AVCaptureDevice.CenterStageControlMode

**Framework**: AVFoundation  
**Kind**: enum

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

## Topics

### Control Modes
- [AVCaptureDevice.CenterStageControlMode.user](avcapturedevice/centerstagecontrolmode-swift.enum/user.md)
  The user controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.app](avcapturedevice/centerstagecontrolmode-swift.enum/app.md)
  The app controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.cooperative](avcapturedevice/centerstagecontrolmode-swift.enum/cooperative.md)
  A user and app cooperatively share control of Center Stage.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/centerstagecontrolmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isCenterStageActive: Bool](avcapturedevice/iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](avcapturedevice/iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](avcapturedevice/centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum)*