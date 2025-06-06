# HKMetadataKeyWeatherTemperature

**Framework**: HealthKit  
**Kind**: var

A key that represents the weather temperature during the sample.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeyWeatherTemperature: String
```

#### Discussion

This key takes an `HKQuantity` value expressed in a unit of temperature. Set this key on an [`HKWorkout`](hkworkout.md) object to represent the overall temperature during the workout.

## See Also

- [let HKMetadataKeyBarometricPressure: String](hkmetadatakeybarometricpressure.md)
  The metadata key for the barometric pressure associated with a sample.
- [let HKMetadataKeyWeatherCondition: String](hkmetadatakeyweathercondition.md)
  A key that represents the weather condition during the sample.
- [let HKMetadataKeyWeatherHumidity: String](hkmetadatakeyweatherhumidity.md)
  A key that represents the weather humidity during the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathertemperature)*