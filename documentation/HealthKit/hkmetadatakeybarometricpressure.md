# HKMetadataKeyBarometricPressure

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The metadata key for the barometric pressure associated with a sample.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let HKMetadataKeyBarometricPressure: String
```

```c
extern NSString * const HKMetadataKeyBarometricPressure;
```

#### Discussion

This key takes an [`HKQuantity`](./hkquantity.md) value that measures the barometric pressure in units of pressure, such as [`atmosphere()`](./hkunit/atmosphere%28%29.md), [`pascal()`](./hkunit/pascal%28%29.md), or [`millimeterOfMercury()`](./hkunit/millimeterofmercury%28%29.md).

## See Also

### Weather Keys
- [let HKMetadataKeyWeatherCondition: String](./hkmetadatakeyweathercondition.md)
  A key that represents the weather condition during the sample.
- [let HKMetadataKeyWeatherHumidity: String](./hkmetadatakeyweatherhumidity.md)
  A key that represents the weather humidity during the sample.
- [let HKMetadataKeyWeatherTemperature: String](./hkmetadatakeyweathertemperature.md)
  A key that represents the weather temperature during the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeybarometricpressure)*