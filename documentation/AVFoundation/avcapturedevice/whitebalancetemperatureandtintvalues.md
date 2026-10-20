# AVCaptureDevice.WhiteBalanceTemperatureAndTintValues

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } AVCaptureWhiteBalanceTemperatureAndTintValues;
```

## Topics

### Accessing standard values
- [static let cloudy: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues/cloudy.md)
  Temperature and tint values ideal for scenes illuminated with natural cloudy daylight.
- [static let daylight: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues/daylight.md)
  Temperature and tint values ideal for scenes illuminated with natural daylight.
- [static let fluorescent: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues/fluorescent.md)
  Temperature and tint values ideal for scenes illuminated with a fluorescent light source.
- [static let shadow: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues/shadow.md)
  Temperature and tint values ideal for scenes illuminated with daylight but in heavy shade.
- [static let tungsten: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues](./whitebalancetemperatureandtintvalues/tungsten.md)
  Temperature and tint values ideal for scenes illuminated with a tungsten light source.
### Creating temperature and tint values
- [init()](./whitebalancetemperatureandtintvalues/init%28%29.md)
  Creates a default value.
- [init(temperature: Float, tint: Float)](./whitebalancetemperatureandtintvalues/init%28temperature,tint%29.md)
  Creates a structure with a white balance temperature and tint.
### Inspecting the values
- [var temperature: Float](./whitebalancetemperatureandtintvalues/temperature.md)
  The white balance color correlated temperature in kelvin.
- [var tint: Float](./whitebalancetemperatureandtintvalues/tint.md)
  The white balance tint value in the range of `-150.0` through `+150.0`.

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
- [AVCaptureDevice.WhiteBalanceChromaticityValues](./whitebalancechromaticityvalues.md)
  A structure that defines CIE 1931 xy chromaticity values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancetemperatureandtintvalues)*