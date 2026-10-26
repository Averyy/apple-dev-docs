# AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines the conditions in which to restrict camera switching.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
struct PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions
```

```c
enum AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions : NSUInteger;
```

#### Overview

Use these constants to control the conditions that allow fallback camera selection when you set the value of the [`primaryConstituentDeviceSwitchingBehavior`](./primaryconstituentdeviceswitchingbehavior-swift.property.md) property to [`AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted`](./primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md).

When triggered by one or more enabled conditions, fallback camera switching waits for exposure and focus to stabilize before deciding which camera to use as the primary constituent device.

Whenever [`videoZoomChanged`](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md) isn’t included in the restricted switching behavior conditions, [`AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted`](./primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md) still allows camera selection when a change in video zoom factor makes a camera eligible or ineligible for selection as the [`activePrimaryConstituent`](./activeprimaryconstituent.md).

When the video zoom factor decreases to below the switch-over zoom factor of the active primary constituent device, the system selects a different camera to satisfy the requested zoom factor.

When the video zoom factor increases and crosses a camera’s switch-over zoom factor, this camera becomes eligible to set as the [`activePrimaryConstituent`](./activeprimaryconstituent.md). If exposure and focus allow, this camera then becomes the new active primary constituent device. Similar to the [`videoZoomChanged`](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md) this also waits for exposure and focus to stabilize. Otherwise the [`activePrimaryConstituent`](./activeprimaryconstituent.md) remains unchanged.

## Topics

### Switching behavior conditions
- [static var exposureModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged.md)
  Restrict switching to a fallback camera only when the device’s exposure mode changes.
- [static var focusModeChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/focusmodechanged.md)
  Restrict switching to a fallback camera only when the device’s focus mode changes.
- [static var videoZoomChanged: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md)
  Restrict switching to a fallback camera only when the device’s video zoom changes.
- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionNone](../avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditions/avcaptureprimaryconstituentdevicerestrictedswitchingbehaviorconditionnone.md)
  Disallow switching to a fallback camera.
### Initializers
- [init(rawValue: UInt)](./primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/init%28rawvalue%29.md)
  Creates a switching behavior condition with an unsigned integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

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
- [var activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](./activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md)
  The conditions that restrict camera switching behavior for the active primary constituent device.
- [var activePrimaryConstituent: AVCaptureDevice?](./activeprimaryconstituent.md)
  A virtual device’s active primary constituent device.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior](./primaryconstituentdeviceswitchingbehavior-swift.enum.md)
  Constants that control when to allow a virtual device to switch its active primary constituent device.
- [var supportedFallbackPrimaryConstituentDevices: [AVCaptureDevice]](./supportedfallbackprimaryconstituentdevices.md)
  The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [var fallbackPrimaryConstituentDevices: [AVCaptureDevice]](./fallbackprimaryconstituentdevices.md)
  The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct)*