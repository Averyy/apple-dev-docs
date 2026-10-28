# AVCaptureDevice.CenterStageControlMode.user

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The user controls Center Stage.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
case user
```

```c
AVCaptureCenterStageControlModeUser
```

## Discussion

In this mode, the user has exclusive control of Center Stage through Control Center. The system throws an exception in this mode if an app attempts to programmatically change the enabled state of Center Stage.

## See Also

### Control modes
- [AVCaptureDevice.CenterStageControlMode.app](./app.md)
  The app controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.cooperative](./cooperative.md)
  A user and app cooperatively share control of Center Stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/user)*