# primaryConstituentDeviceSwitchingBehaviorForRecording

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The camera switching behavior to use for recording.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior { get }
```

```objc
@property (nonatomic, readonly) AVCapturePrimaryConstituentDeviceSwitchingBehavior primaryConstituentDeviceSwitchingBehaviorForRecording;
```

## Discussion

The default value of this property is [`AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted`](../avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md).

This property is key-value observable.

## See Also

### Restricting camera switching
- [var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool](./isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md)
  A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](./setprimaryconstituentdeviceswitchingbehaviorforrecording%28_,restrictedswitchingbehaviorconditions%29.md)
  Sets the camera switching behavior to use during recording.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md)
  The conditions during which camera switching may occur while recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording)*