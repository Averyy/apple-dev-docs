# setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues:handler:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Discussion

This method takes a [`AVCaptureDevice.WhiteBalanceTemperatureAndTintValues`](avcapturedevice/whitebalancetemperatureandtintvalues.md) struct and applies the appropriate [`AVCaptureDevice.WhiteBalanceGains`](avcapturedevice/whitebalancegains.md). This method throws an `NSRangeException` if any of the values are set to an unsupported level. This method throws an `NSGenericException` if called without first obtaining exclusive access to the device using [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md).

## Parameters

- `whiteBalanceTemperatureAndTintValues`: The white balance temperature and tint values, as computed from   method,   presets or manual input.
- `handler`: A block to be called when white balance values have been set to the values specified and   is set to  . If   is called multiple times, the completion handlers are called in FIFO order. The block receives a timestamp which matches that of the first buffer to which all settings have been applied. Note that the timestamp is synchronized to the device clock, and thus must be converted to the   prior to comparison with the timestamps of buffers delivered via an  . This parameter may be   if synchronization is not required.

## See Also

- [var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool](avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.md)
  A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [func setWhiteBalanceModeLocked(with: AVCaptureDevice.WhiteBalanceGains, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setwhitebalancemodelocked(with:completionhandler:).md)
  Sets the white balance to locked mode with the specified white balance gains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues:handler:))*