# deviceWhiteBalanceGains(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Converts device-independent temperature and tint values to device-specific white balance RGB gain values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func deviceWhiteBalanceGains(for tempAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains
```

```objc
- (AVCaptureWhiteBalanceGains) deviceWhiteBalanceGainsForTemperatureAndTintValues:(AVCaptureWhiteBalanceTemperatureAndTintValues) tempAndTintValues;
```

## Return Value

A fully populated [`AVCaptureDevice.WhiteBalanceGains`](./whitebalancegains.md) structure containing device-specific RGB gain values.

## Discussion

Call this method to convert device-independent temperature and tint values to device-specific RGB white balance gain values.

You may pass any temperature and tint values and corresponding white balance gains will be produced. Note, though, that some temperature and tint combinations yield out-of-range device RGB values that will cause an exception to be thrown if passed directly to [`setWhiteBalanceModeLocked(with:completionHandler:)`](./setwhitebalancemodelocked%28with,completionhandler%29.md).  Be sure to verify that the red, green, and blue gain values are within the range of [`1.0` - [`maxWhiteBalanceGain`](./maxwhitebalancegain.md)].

## Parameters

- `tempAndTintValues`: An [`AVCaptureDevice.WhiteBalanceTemperatureAndTintValues`](./whitebalancetemperatureandtintvalues.md) structure containing the temperature and tint values.

## See Also

### Performing conversions
- [func chromaticityValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceChromaticityValues](./chromaticityvalues%28for%29.md)
  Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./temperatureandtintvalues%28for%29.md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains%28for%29-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](./whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceChromaticityValues](./whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicewhitebalancegains(for:)-3wtsa)*