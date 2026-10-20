# AVCaptureDevice.WhiteBalanceChromaticityValues

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines CIE 1931 xy chromaticity values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
struct WhiteBalanceChromaticityValues
```

```c
typedef struct { ... } AVCaptureWhiteBalanceChromaticityValues;
```

## Topics

### Creating chromaticity values
- [init()](./whitebalancechromaticityvalues/init%28%29.md)
  Creates a structure for white balance chromaticity values.
- [init(x: Float, y: Float)](./whitebalancechromaticityvalues/init%28x,y%29.md)
  Creates a structure for white balance chromaticity values from its x and y coordinates.
### Inspecting the values
- [var x: Float](./whitebalancechromaticityvalues/x.md)
  The x component of the CIE 1931 chromaticity value.
- [var y: Float](./whitebalancechromaticityvalues/y.md)
  The y component of the CIE 1931 chromaticity value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Performing conversions
- [func chromaticityValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceChromaticityValues](./chromaticityvalues%28for%29.md)
  Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./temperatureandtintvalues%28for%29.md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains%28for%29-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains](./devicewhitebalancegains%28for%29-3wtsa.md)
  Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](./whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues)*