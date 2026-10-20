# AVCaptureDevice.WhiteBalanceGains

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } AVCaptureWhiteBalanceGains;
```

## Topics

### Creating white balance gains
- [init()](./whitebalancegains/init%28%29.md)
  The default initializer for white balance gains.
- [init(redGain: Float, greenGain: Float, blueGain: Float)](./whitebalancegains/init%28redgain,greengain,bluegain%29.md)
  Initializes a white balance gain from its red, green, and blue gain components.
### Isolating gain by color channel
- [var blueGain: Float](./whitebalancegains/bluegain.md)
  The blue gain component of the white balance value.
- [var greenGain: Float](./whitebalancegains/greengain.md)
  The green gain component of the white balance value.
- [var redGain: Float](./whitebalancegains/redgain.md)
  The red gain component of the white balance value.

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
- [AVCaptureDevice.WhiteBalanceChromaticityValues](./whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.
- [AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues.md)
  A structure that defines temperature and tint values correlated to a white-balance color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancegains)*