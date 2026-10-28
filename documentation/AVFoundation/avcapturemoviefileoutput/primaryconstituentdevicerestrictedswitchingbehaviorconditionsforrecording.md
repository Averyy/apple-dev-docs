# primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The conditions during which camera switching may occur while recording.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

```objc
@property (nonatomic, readonly) AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording;
```

## Discussion

The default conditions include [`videoZoomChanged`](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md), [`focusModeChanged`](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/focusmodechanged.md), and [`exposureModeChanged`](../avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged.md).

This property is key-value observable.

## See Also

### Restricting camera switching
- [var isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled: Bool](./isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md)
  A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [func setPrimaryConstituentDeviceSwitchingBehaviorForRecording(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](./setprimaryconstituentdeviceswitchingbehaviorforrecording%28_,restrictedswitchingbehaviorconditions%29.md)
  Sets the camera switching behavior to use during recording.
- [var primaryConstituentDeviceSwitchingBehaviorForRecording: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./primaryconstituentdeviceswitchingbehaviorforrecording.md)
  The camera switching behavior to use for recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording)*