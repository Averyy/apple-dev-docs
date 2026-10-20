# AVCaptureDevice.CenterStageControlMode.cooperative

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

A user and app cooperatively share control of Center Stage.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.3+
- tvOS 17.0+

## Declaration

```swift
case cooperative
```

```c
AVCaptureCenterStageControlModeCooperative
```

#### Discussion

In this mode, it’s your app’s responsibilitiy to honor user intent and make center stage active when they request. Because the user can change the enabled state through Control Center, key-value observe the [`isCenterStageEnabled`](../iscenterstageenabled.md) property value and update your app state appropriately.

## See Also

### Control modes
- [AVCaptureDevice.CenterStageControlMode.user](./user.md)
  The user controls Center Stage.
- [AVCaptureDevice.CenterStageControlMode.app](./app.md)
  The app controls Center Stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/cooperative)*