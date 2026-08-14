# isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

Use this property to enable camera switching restrictions when recording movies. You set restrictions by calling the output’s [`setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)`](avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:).md) method. The restrictions take effect when you start recording, and revert to the behavior set by the capture device’s [`primaryConstituentDeviceSwitchingBehavior`](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md) when you stop recording.

By default, this property is [`true`](https://developer.apple.com/documentation/swift/true) when connected to a capture device that supports constituent device switching.

## See Also

- [func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:).md)
  Sets the camera switching behavior to use during recording.
- [var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording.md)
  The camera switching behavior to use for recording.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md)
  The conditions during which camera switching may occur while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled)*