# currentWhiteBalanceGains

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A special constant representing the current white balance setting.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let currentWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains
```

```c
extern const AVCaptureWhiteBalanceGains AVCaptureWhiteBalanceGainsCurrent;
```

## Discussion

Pass this value to [`setWhiteBalanceModeLocked(with:completionHandler:)`](./setwhitebalancemodelocked%28with,completionhandler%29.md) to lock white balance gains to their current value (that is, disable automatic white balancing).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentwhitebalancegains)*