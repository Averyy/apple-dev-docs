# centerStageControlMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A value that indicates the current mode of Center Stage control.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode { get set }
```

```objc
@property (class) AVCaptureCenterStageControlMode centerStageControlMode;
```

#### Discussion

See Control Modes for details on choosing an appropriate control mode.

## See Also

### Configuring Center Stage
- [var isCenterStageActive: Bool](./iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](./iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](./centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [AVCaptureDevice.CenterStageControlMode](./centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.
- [centerStageRectOfInterestSupported](./centerstagerectofinterestsupported.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.type.property)*