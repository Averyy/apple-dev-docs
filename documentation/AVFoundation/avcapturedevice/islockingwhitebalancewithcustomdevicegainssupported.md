# isLockingWhiteBalanceWithCustomDeviceGainsSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device supports locking white balance to specific gain values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLockingWhiteBalanceWithCustomDeviceGainsSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLockingWhiteBalanceWithCustomDeviceGainsSupported) BOOL lockingWhiteBalanceWithCustomDeviceGainsSupported;
```

#### Discussion

If the value is [`false`](../../Swift/false.md), calling the [`setWhiteBalanceModeLocked(with:completionHandler:)`](./setwhitebalancemodelocked%28with,completionhandler%29.md) method with a white balance gains value other than [`currentWhiteBalanceGains`](./currentwhitebalancegains.md) throws an exception.

## See Also

### Setting white balance manually
- [func setWhiteBalanceModeLocked(with: AVCaptureDevice.WhiteBalanceGains, completionHandler: ((CMTime) -> Void)?)](./setwhitebalancemodelocked%28with,completionhandler%29.md)
  Sets the white balance to locked mode with the specified white balance gains.
- [func setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues, handler: ((CMTime) -> Void)?)](./setwhitebalancemodelocked%28whitebalancetemperatureandtintvalues,handler%29.md)
  Sets white balance to locked mode with explicit temperature and tint values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported)*