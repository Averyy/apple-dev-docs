# AVCaptureDevice.WhiteBalanceGains

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines RGB white balance gain values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
struct WhiteBalanceGains
```

## Topics

### Creating White Balance Gains
- [init()](avcapturedevice/whitebalancegains/init.md)
  The default initializer for white balance gains.
- [init(redGain: Float, greenGain: Float, blueGain: Float)](avcapturedevice/whitebalancegains/init(redgain:greengain:bluegain:).md)
  Initializes a white balance gain from its red, green, and blue gain components.
### Isolating Gain by Color Channel
- [var blueGain: Float](avcapturedevice/whitebalancegains/bluegain.md)
  The blue gain component of the white balance value.
- [var greenGain: Float](avcapturedevice/whitebalancegains/greengain.md)
  The green gain component of the white balance value.
- [var redGain: Float](avcapturedevice/whitebalancegains/redgain.md)
  The red gain component of the white balance value.

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
- [AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancegains)*