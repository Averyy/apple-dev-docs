# exposureModeChanged

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Restrict switching to a fallback camera only when the device’s exposure mode changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
static var exposureModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

```c
AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionExposureModeChanged
```

## See Also

### Switching behavior conditions
- [static var focusModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./focusmodechanged.md)
  Restrict switching to a fallback camera only when the device’s focus mode changes.
- [static var videoZoomChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./videozoomchanged.md)
  Restrict switching to a fallback camera only when the device’s video zoom changes.
- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionNone](../../avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditions/avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditionnone.md)
  Disallow switching to a fallback camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged)*