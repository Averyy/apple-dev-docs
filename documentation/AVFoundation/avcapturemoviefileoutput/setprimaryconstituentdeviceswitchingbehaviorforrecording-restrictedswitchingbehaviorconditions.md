# setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)

**Framework**: AVFoundation  
**Kind**: method

Sets the camera switching behavior to use during recording.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_ switchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)
```

#### Discussion

Use this method to control the camera switching behavior the system uses when recording a movie. The behavior you specify takes effect when you enable it by setting the value of [`isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled`](avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) to [`true`](https://developer.apple.com/documentation/Swift/true).

When a capture device doesn’t support constituent device selection, attempting to set a behavior other than [`AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported`](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported.md) causes the system to throw an invalid argument exception.

## Parameters

- `switchingBehavior`: Attempting to restrict the switching behavior of a capture device that doesn’t support constituent device switching results in an error.
- `restrictedSwitchingBehaviorConditions`: The conditions during which camera switching occurs. Only set a condition when you set the switching behavior to  . In all other cases, set the value to  .

## See Also

- [var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool](avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md)
  A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording.md)
  The camera switching behavior to use for recording.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md)
  The conditions during which camera switching may occur while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:))*