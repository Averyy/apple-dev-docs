# videoZoomChanged

**Framework**: AVFoundation  
**Kind**: property

Restrict switching to a fallback camera only when the device’s video zoom changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
static var videoZoomChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

#### Discussion

This condition switches cameras when the video zoom factor changes, either by setting a value for the device’s [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property or calling its [`ramp(toVideoZoomFactor:withRate:)`](avcapturedevice/ramp(tovideozoomfactor:withrate:).md) method.

> **Note**:  All changes to video zoom factor allow switching to a fallback camera, not only those changes across switch-over zoom factors.

 All changes to video zoom factor allow switching to a fallback camera, not only those changes across switch-over zoom factors.

## See Also

- [static var exposureModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged.md)
  Restrict switching to a fallback camera only when the device’s exposure mode changes.
- [static var focusModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/focusmodechanged.md)
  Restrict switching to a fallback camera only when the device’s focus mode changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged)*