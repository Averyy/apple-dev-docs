# AVCaptureDevice.WhiteBalanceChromaticityValues

**Framework**: AVFoundation  
**Kind**: struct

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

## Topics

### Creating Chromaticity Values
- [init()](avcapturedevice/whitebalancechromaticityvalues/init.md)
  Creates a structure for white balance chromaticity values.
- [init(x: Float, y: Float)](avcapturedevice/whitebalancechromaticityvalues/init(x:y:).md)
  Creates a structure for white balance chromaticity values from its x and y coordinates.
### Inspecting the Values
- [var x: Float](avcapturedevice/whitebalancechromaticityvalues/x.md)
  The x component of the CIE 1931 chromaticity value.
- [var y: Float](avcapturedevice/whitebalancechromaticityvalues/y.md)
  The y component of the CIE 1931 chromaticity value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func chromaticityValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/chromaticityvalues(for:).md)
  Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [func temperatureAndTintValues(for: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/temperatureandtintvalues(for:).md)
  Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-9gdtw.md)
  Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [func deviceWhiteBalanceGains(for: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains](avcapturedevice/devicewhitebalancegains(for:)-3wtsa.md)
  Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [AVCaptureDevice.WhiteBalanceGains](avcapturedevice/whitebalancegains.md)
  A structure that defines RGB white balance gain values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues)*