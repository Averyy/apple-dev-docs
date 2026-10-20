# setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues:handler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets white balance to locked mode with explicit temperature and tint values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+

## Declaration

```swift
func setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues, handler: ((CMTime) -> Void)? = nil)
```

```objc
- (void) setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:(AVCaptureWhiteBalanceTemperatureAndTintValues) whiteBalanceTemperatureAndTintValues completionHandler:(void (^)(CMTime syncTime)) handler;
```

#### Discussion

This method takes a [`AVCaptureDevice.WhiteBalanceTemperatureAndTintValues`](./whitebalancetemperatureandtintvalues.md) struct and applies the appropriate [`AVCaptureDevice.WhiteBalanceGains`](./whitebalancegains.md). This method throws an `NSRangeException` if any of the values are set to an unsupported level. This method throws an `NSGenericException` if called without first obtaining exclusive access to the device using [`lockForConfiguration()`](./lockforconfiguration%28%29.md).

## Parameters

- `whiteBalanceTemperatureAndTintValues`: The white balance temperature and tint values, as computed from [`temperatureAndTintValues(for:)`](./temperatureandtintvalues%28for%29.md) method, [`AVCaptureDevice.WhiteBalanceTemperatureAndTintValues`](./whitebalancetemperatureandtintvalues.md) presets or manual input.
- `handler`: A block to be called when white balance values have been set to the values specified and [`whiteBalanceMode`](./whitebalancemode-swift.property.md) is set to `AVCaptureWhiteBalanceModeLocked`. If [`setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues:handler:)`](./setwhitebalancemodelocked%28whitebalancetemperatureandtintvalues,handler%29.md) is called multiple times, the completion handlers are called in FIFO order. The block receives a timestamp which matches that of the first buffer to which all settings have been applied. Note that the timestamp is synchronized to the device clock, and thus must be converted to the [`synchronizationClock`](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered via an [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md). This parameter may be `nil` if synchronization is not required.

## See Also

### Setting white balance manually
- [var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool](./islockingwhitebalancewithcustomdevicegainssupported.md)
  A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [func setWhiteBalanceModeLocked(with: AVCaptureDevice.WhiteBalanceGains, completionHandler: ((CMTime) -> Void)?)](./setwhitebalancemodelocked%28with,completionhandler%29.md)
  Sets the white balance to locked mode with the specified white balance gains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues:handler:))*