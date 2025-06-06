# isLockingWhiteBalanceWithCustomDeviceGainsSupported

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

If the value is [`false`](https://developer.apple.com/documentation/swift/false), calling the [`setWhiteBalanceModeLocked(with:completionHandler:)`](avcapturedevice/setwhitebalancemodelocked(with:completionhandler:).md) method with a white balance gains value other than [`currentWhiteBalanceGains`](avcapturedevice/currentwhitebalancegains.md) throws an exception.

## See Also

- [func setWhiteBalanceModeLocked(with: AVCaptureDevice.WhiteBalanceGains, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setwhitebalancemodelocked(with:completionhandler:).md)
  Sets the white balance to locked mode with the specified white balance gains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported)*