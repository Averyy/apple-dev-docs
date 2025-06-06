# setPrimaryConstituentDeviceSwitchingBehavior(_:restrictedSwitchingBehaviorConditions:)

**Framework**: AVFoundation  
**Kind**: method

Sets the switching behavior of the primary constituent device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
func setPrimaryConstituentDeviceSwitchingBehavior(_ switchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)
```

#### Discussion

Use this method to configure the camera switching behavior of a capture device. Before calling it, determine if a device supports configuring its device switching behavior by querying the device’s [`activePrimaryConstituentDeviceSwitchingBehavior`](avcapturedevice/activeprimaryconstituentdeviceswitchingbehavior.md) property. If the value equals `.unsupported`, attempting to configure its switching behavior results in an error.

```swift
// Exit early if the device doesn't support configuring switching behavior.
guard captureDevice.activePrimaryConstituentDeviceSwitchingBehavior != .unsupported else { return }
captureDevice.setPrimaryConstituentDeviceSwitchingBehavior(.auto, restrictedSwitchingBehaviorConditions: [])
```

When recording using an instance of [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md), you may override the switching behavior by calling the movie file output’s [`setPrimaryConstituentDeviceSwitchingBehaviorForRecording(_:restrictedSwitchingBehaviorConditions:)`](avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(_:restrictedswitchingbehaviorconditions:).md) method.

## Parameters

- `switchingBehavior`: The switching behavior to set on the device.
- `restrictedSwitchingBehaviorConditions`: Setting the switching behavior to a value other than   requires that you set this argument to an empty option set.

## See Also

- [var primaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md)
  The switching behavior for the primary constituent device.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md)
  The conditions that restrict the primary constituent device’s switching behavior.
- [var activePrimaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/activeprimaryconstituentdeviceswitchingbehavior.md)
  The switching behavior of the active constituent device.
- [var activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md)
  The conditions that restrict camera switching behavior for the active primary constituent device.
- [var activePrimaryConstituent: AVCaptureDevice?](avcapturedevice/activeprimaryconstituent.md)
  A virtual device’s active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum.md)
  Constants that control when to allow a virtual device to switch its active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md)
  A structure that defines the conditions in which to restrict camera switching.
- [var supportedFallbackPrimaryConstituentDevices: [AVCaptureDevice]](avcapturedevice/supportedfallbackprimaryconstituentdevices.md)
  The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [var fallbackPrimaryConstituentDevices: [AVCaptureDevice]](avcapturedevice/fallbackprimaryconstituentdevices.md)
  The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setprimaryconstituentdeviceswitchingbehavior(_:restrictedswitchingbehaviorconditions:))*