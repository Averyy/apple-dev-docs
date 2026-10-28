# activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The conditions that restrict camera switching behavior for the active primary constituent device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions { get }
```

```objc
@property (nonatomic, readonly) AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions;
```

## Discussion

For virtual devices with multiple constituent devices, this property returns the active restricted switching behavior conditions. This is equal to [`primaryConstituentDeviceRestrictedSwitchingBehaviorConditions`](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md) except while recording using an [`AVCaptureMovieFileOutput`](../avcapturemoviefileoutput.md) that you configure with different restricted switching behavior conditions.

Devices that don’t support constituent device switching return [`AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionNone`](../avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditions/avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditionnone.md).

This property is key-value observable.

## See Also

### Restricting camera switching
- [func setPrimaryConstituentDeviceSwitchingBehavior(AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)](./setprimaryconstituentdeviceswitchingbehavior%28_,restrictedswitchingbehaviorconditions%29.md)
  Sets the switching behavior of the primary constituent device.
- [var primaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./primaryconstituentdeviceswitchingbehavior-swift.property.md)
  The switching behavior for the primary constituent device.
- [var primaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md)
  The conditions that restrict the primary constituent device’s switching behavior.
- [var activePrimaryConstituentDeviceSwitchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./activeprimaryconstituentdeviceswitchingbehavior.md)
  The switching behavior of the active constituent device.
- [var activePrimaryConstituent: AVCaptureDevice?](./activeprimaryconstituent.md)
  A virtual device’s active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./primaryconstituentdeviceswitchingbehavior-swift.enum.md)
  Constants that control when to allow a virtual device to switch its active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md)
  A structure that defines the conditions in which to restrict camera switching.
- [var supportedFallbackPrimaryConstituentDevices: [AVCaptureDevice]](./supportedfallbackprimaryconstituentdevices.md)
  The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [var fallbackPrimaryConstituentDevices: [AVCaptureDevice]](./fallbackprimaryconstituentdevices.md)
  The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions)*