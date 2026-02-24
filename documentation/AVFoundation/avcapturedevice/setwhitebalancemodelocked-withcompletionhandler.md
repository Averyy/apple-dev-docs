# setWhiteBalanceModeLocked(with:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Sets the white balance to locked mode with the specified white balance gains.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setWhiteBalanceModeLocked(with whiteBalanceGains: AVCaptureDevice.WhiteBalanceGains) async -> CMTime
```

#### Discussion

Each channel in the white balance gains structure supports values between `1.0` and [`maxWhiteBalanceGain`](avcapturedevice/maxwhitebalancegain.md). Setting a channel value outside this range generates an exception.

The system normalizes gain values to the minimum channel value to avoid brightness changes (for example, `R:2 G:2 B:4` normalizes to `R:1 G:1 B:2`).

Before changing the value the white balance gains, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock and allow other devices to configure the settings.

## Parameters

- `whiteBalanceGains`: The white balance gains to set. Pass a value of [`currentWhiteBalanceGains`](avcapturedevice/currentwhitebalancegains.md) to leave the current white balance unchanged.
- `handler`: A callback the system invokes when the adjustment to the white balance is complete and the [`whiteBalanceMode`](avcapturedevice/whitebalancemode-swift.property.md) set to a locked state. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [`synchronizationClock`](avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## Topics

### White balance constants
- [class let currentWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](avcapturedevice/currentwhitebalancegains.md)
  A special constant representing the current white balance setting.

## See Also

- [var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool](avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.md)
  A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [func setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues, handler: ((CMTime) -> Void)?)](avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues:handler:).md)
  Sets white balance to locked mode with explicit temperature and tint values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(with:completionhandler:))*