# chromaticityValues(for:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Return Value

A structure that contains device-independent values.

#### Discussion

Call this method to convert device-specific white balance RGB gain values to device-independent chromaticity (little x, little y) values.

Each change in the structure supports values between `1.0` and [`maxWhiteBalanceGain`](avcapturedevice/maxwhitebalancegain.md). This method throws an exception if you specify an unsupported value.

## Parameters

- `whiteBalanceGains`: The white balance gain values. You can’t specify a value of  .

## See Also

- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/temperatureandtintvalues(for:).md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-3wtsa.md)
  Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](avcapturedevice/whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/chromaticityvalues(for:))*