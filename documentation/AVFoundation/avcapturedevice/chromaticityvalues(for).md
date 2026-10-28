# chromaticityValues(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts device-specific white balance RGB gain values to device-independent chromaticity values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func chromaticityValues(for whiteBalanceGains: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceChromaticityValues
```

```objc
- (AVCaptureWhiteBalanceChromaticityValues) chromaticityValuesForDeviceWhiteBalanceGains:(AVCaptureWhiteBalanceGains) whiteBalanceGains;
```

## Return Value

A structure that contains device-independent values.

## Discussion

Call this method to convert device-specific white balance RGB gain values to device-independent chromaticity (little x, little y) values.

Each change in the structure supports values between `1.0` and [`maxWhiteBalanceGain`](./maxwhitebalancegain.md). This method throws an exception if you specify an unsupported value.

## Parameters

- `whiteBalanceGains`: The white balance gain values. You can’t specify a value of [`currentWhiteBalanceGains`](./currentwhitebalancegains.md).

## See Also

### Performing conversions
- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./temperatureandtintvalues%28for%29.md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains%28for%29-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains%28for%29-3wtsa.md)
  Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](./whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceChromaticityValues](./whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/chromaticityvalues(for:))*