# AVCaptureDevice.WhiteBalanceTemperatureAndTintValues

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines temperature and tint values correlated to a white-balance color.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
struct WhiteBalanceTemperatureAndTintValues
```

## Topics

### Accessing standard values
- [static let cloudy: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues/cloudy.md)
  Temperature and tint values ideal for scenes illuminated with natural cloudy daylight.
- [static let daylight: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues/daylight.md)
  Temperature and tint values ideal for scenes illuminated with natural daylight.
- [static let fluorescent: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues/fluorescent.md)
  Temperature and tint values ideal for scenes illuminated with a fluorescent light source.
- [static let shadow: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues/shadow.md)
  Temperature and tint values ideal for scenes illuminated with daylight but in heavy shade.
- [static let tungsten: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues/tungsten.md)
  Temperature and tint values ideal for scenes illuminated with a tungsten light source.
### Creating temperature and tint values
- [init()](avcapturedevice/whitebalancetemperatureandtintvalues/init.md)
  Creates a default value.
- [init(temperature: Float, tint: Float)](avcapturedevice/whitebalancetemperatureandtintvalues/init(temperature:tint:).md)
  Creates a structure with a white balance temperature and tint.
### Inspecting the values
- [var temperature: Float](avcapturedevice/whitebalancetemperatureandtintvalues/temperature.md)
  The white balance color correlated temperature in kelvin.
- [var tint: Float](avcapturedevice/whitebalancetemperatureandtintvalues/tint.md)
  The white balance tint value in the range of `-150.0` through `+150.0`.

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
- [AVCaptureDevice.WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancetemperatureandtintvalues)*