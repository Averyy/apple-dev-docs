# HKMetadataKeyAlpineSlopeGrade

**Framework**: HealthKit  
**Kind**: var

A key that indicates the percent slope of a ski run.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
let HKMetadataKeyAlpineSlopeGrade: String
```

## Mentions

- [Receiving Downhill Skiing and Snowboarding Data](receiving-downhill-skiing-and-snowboarding-data.md)

#### Discussion

Set this key on quantity samples that represent distance, or on workout segments. Set its value to an [`HKQuantity`](hkquantity.md) object with a percent unit, where 100% indicates a 45 degree slope.

HealthKit assigns this metadata key to the segments it automatically creates for [`HKWorkoutActivityType.downhillSkiing`](hkworkoutactivitytype/downhillskiing.md) and [`HKWorkoutActivityType.snowboarding`](hkworkoutactivitytype/snowboarding.md) workout sessions (Apple Watch Series 3 only).

## See Also

- [let HKMetadataKeyElevationAscended: String](hkmetadatakeyelevationascended.md)
  A key that indicates the cumulative elevation ascended during a workout.
- [let HKMetadataKeyElevationDescended: String](hkmetadatakeyelevationdescended.md)
  A key that indicates the cumulative elevation descended during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyalpineslopegrade)*