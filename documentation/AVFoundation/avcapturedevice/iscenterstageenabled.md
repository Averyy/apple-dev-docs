# isCenterStageEnabled

**Framework**: Avfoundation  
**Kind**: property

A Boolean value that indicates whether a user or an app enabled Center Stage on a device.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
class var isCenterStageEnabled: Bool { get set }
```

#### Discussion

You can only set this value when Center Stage is under app or cooperative control. Attempting to change the enabled state when the control mode is [`AVCaptureDevice.CenterStageControlMode.user`](avcapturedevice/centerstagecontrolmode-swift.enum/user.md), results in the system throwing an exception.

> **Note**:  When Center Stage is under user or cooperative control, the user may change the feature’s enabled state in Control Center. Key-value observe this property value to monitor these changes.

## See Also

- [var isCenterStageActive: Bool](avcapturedevice/iscenterstageactive.md)
  A Boolean value that indicates whether Center Stage is active on a device.
- [var centerStageRectOfInterest: CGRect](avcapturedevice/centerstagerectofinterest.md)
  The effective region within the output pixel buffer to perform Center Stage framing.
- [class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md)
  A value that indicates the current mode of Center Stage control.
- [AVCaptureDevice.CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md)
  Constants that indicate the current Center Stage control mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscenterstageenabled)*