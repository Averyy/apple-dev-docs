# setPrimaryConstituentDeviceSwitchingBehaviorLockedWith(_:)

**Framework**: AVFoundation  
**Kind**: method

Sets the switching behavior of the primary constituent device to locked with the specified device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
func setPrimaryConstituentDeviceSwitchingBehaviorLockedWith(_ device: AVCaptureDevice)
```

#### Discussion

Before locking a virtual camera’s primary constituent device, check that [`isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported`](avcapturedevice/isprimaryconstituentdeviceswitchingbehaviorlockedwithdevicesupported.md) is `true`. If locking is not supported, attempting to lock throws an `NSInvalidArgumentException`. Call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Once a constituent device is locked, it becomes the [`activePrimaryConstituent`](avcapturedevice/activeprimaryconstituent.md), and [`primaryConstituentDeviceSwitchingBehavior`](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md) is updated to `AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked`. The virtual camera’s properties remain unchanged. Their effective values can be obtained from the [`activePrimaryConstituent`](avcapturedevice/activeprimaryconstituent.md). To unlock the primary constituent device, set [`primaryConstituentDeviceSwitchingBehavior`](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.property.md) to `AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto`. This may trigger an immediate update of [`activePrimaryConstituent`](avcapturedevice/activeprimaryconstituent.md). Locking a different primary constituent device without first unlocking the current one is allowed.

If the current [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) is within the constituent device’s supported range, it will remain unchanged. If it falls outside the range, the zoom factor will automatically be clamped to the nearest supported value. If a zoom ramp is in progress, the ramp target and current position will similarly be updated to stay within the supported range.  If both the target and position are thus clamped to the same value, this will cancel the ramp at that value, otherwise the ramp will continue within the remaining available range at its current velocity.

## Parameters

- `device`: The constituent device to lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setprimaryconstituentdeviceswitchingbehaviorlockedwith(_:))*