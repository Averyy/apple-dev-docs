# maxWhiteBalanceGain

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum supported value to which you can set a color channel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var maxWhiteBalanceGain: Float { get }
```

```objc
@property (nonatomic, readonly) float maxWhiteBalanceGain;
```

## Discussion

This property doesn’t change for the life of the object.

## See Also

### Inspecting gain levels
- [var deviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains.md)
  The current device-specific RGB white balance gain values in use.
- [var grayWorldDeviceWhiteBalanceGains: AVCaptureDevice.WhiteBalanceGains](./grayworlddevicewhitebalancegains.md)
  The current device-specific white balance values required for a neutral gray white point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxwhitebalancegain)*