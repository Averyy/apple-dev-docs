# HKMetadataKeyWeatherHumidity

**Framework**: HealthKit  
**Kind**: var

A key that represents the weather humidity during the sample.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeyWeatherHumidity: String
```

#### Discussion

This key takes an `HKQuantity` value expressed as a percentage. Set this key on an [`HKWorkout`](hkworkout.md) object to represent the overall humidity during the workout.

## See Also

- [let HKMetadataKeyBarometricPressure: String](hkmetadatakeybarometricpressure.md)
  The metadata key for the barometric pressure associated with a sample.
- [let HKMetadataKeyWeatherCondition: String](hkmetadatakeyweathercondition.md)
  A key that represents the weather condition during the sample.
- [let HKMetadataKeyWeatherTemperature: String](hkmetadatakeyweathertemperature.md)
  A key that represents the weather temperature during the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweatherhumidity)*