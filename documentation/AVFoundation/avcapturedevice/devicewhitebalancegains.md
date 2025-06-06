# deviceWhiteBalanceGains

**Framework**: AVFoundation  
**Kind**: property

The current device-specific RGB white balance gain values in use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var deviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains { get }
```

#### Discussion

This property specifies the current red, green, and blue gain values used for white balance. You can use the values to adjust color casts for a given scene. Each channel supports values between 1.0 and -[`maxWhiteBalanceGain`](avcapturedevice/maxwhitebalancegain.md).

This property is key-value observable.

## See Also

- [var grayWorldDeviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](avcapturedevice/grayworlddevicewhitebalancegains.md)
  The current device-specific white balance values required for a neutral gray white point.
- [var maxWhiteBalanceGain: Float](avcapturedevice/maxwhitebalancegain.md)
  The maximum supported value to which you can set a color channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicewhitebalancegains)*