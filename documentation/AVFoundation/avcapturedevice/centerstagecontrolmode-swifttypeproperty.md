# centerStageControlMode

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

See Control Modes for details on choosing an appropriate control mode.

## See Also

- [var isCenterStageActive: Bool](avcapturedevice/iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [class var isCenterStageEnabled: Bool](avcapturedevice/iscenterstageenabled.md)
  A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [var centerStageRectOfInterest: CGRect](avcapturedevice/centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.type.property)*