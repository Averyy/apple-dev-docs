# HKMetadataKeyWeatherCondition

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

A key that represents the weather condition during the sample.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeyWeatherCondition: String
```

```c
extern NSString * const HKMetadataKeyWeatherCondition;
```

#### Discussion

This key takes an an [`NSNumber`](../Foundation/nsnumber.md) value that contains an [`HKWeatherCondition`](./hkweathercondition.md) value. Set this key on an [`HKWorkout`](./hkworkout.md) object to represent the overall weather condition during the workout.

## Topics

### Valid Weather Conditions
- [enum HKWeatherCondition](./hkweathercondition.md)
  Constants that indicate a type of weather.

## See Also

### Weather Keys
- [let HKMetadataKeyBarometricPressure: String](./hkmetadatakeybarometricpressure.md)
  The metadata key for the barometric pressure associated with a sample.
- [let HKMetadataKeyWeatherHumidity: String](./hkmetadatakeyweatherhumidity.md)
  A key that represents the weather humidity during the sample.
- [let HKMetadataKeyWeatherTemperature: String](./hkmetadatakeyweathertemperature.md)
  A key that represents the weather temperature during the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathercondition)*