# isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to restrict constituent device switching behavior during recording.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled) BOOL primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled;
```

## Discussion

Use this property to enable camera switching restrictions when recording movies. You set restrictions by calling the output’s [`setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)`](./setprimaryconstituentdeviceswitchingbehaviorforrecording%28_,restrictedswitchingbehaviorconditions%29.md) method. The restrictions take effect when you start recording, and revert to the behavior set by the capture device’s [`primaryConstituentDeviceSwitchingBehavior`](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md) when you stop recording.

By default, this property is [`true`](../../Swift/true.md) when connected to a capture device that supports constituent device switching.

## See Also

### Restricting camera switching
- [func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](./setprimaryconstituentdeviceswitchingbehaviorforrecording%28_,restrictedswitchingbehaviorconditions%29.md)
  Sets the camera switching behavior to use during recording.
- [var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./primaryconstituentdeviceswitchingbehaviorforrecording.md)
  The camera switching behavior to use for recording.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md)
  The conditions during which camera switching may occur while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled)*