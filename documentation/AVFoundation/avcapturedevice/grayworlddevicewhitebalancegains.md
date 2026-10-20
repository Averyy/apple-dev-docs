# grayWorldDeviceWhiteBalanceGains

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The current device-specific white balance values required for a neutral gray white point.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var grayWorldDeviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains { get }
```

```objc
@property (nonatomic, readonly) AVCaptureWhiteBalanceGains grayWorldDeviceWhiteBalanceGains;
```

#### Discussion

This property specifies the current red, green, and blue gain values derived from the current scene to deliver a neutral (or gray world) white point for white balance.

Gray world values assume you’ve placed a neutral subject (for example, a gray card) in the middle of the subject area, and fills the center 50% of the frame. Apps can read these values and apply them to the device using [`setWhiteBalanceModeLocked(with:completionHandler:)`](./setwhitebalancemodelocked%28with,completionhandler%29.md).

Each change supports values between `1.0` and [`maxWhiteBalanceGain`](./maxwhitebalancegain.md). You can read the value at any time, regardless of white balance mode.

This property is key-value observable.

## See Also

### Inspecting gain levels
- [var deviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains.md)
  The current device-specific RGB white balance gain values in use.
- [var maxWhiteBalanceGain: Float](./maxwhitebalancegain.md)
  The maximum supported value to which you can set a color channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/grayworlddevicewhitebalancegains)*