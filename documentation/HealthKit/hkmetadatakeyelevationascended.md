# HKMetadataKeyElevationAscended

**Framework**: HealthKit  
**Kind**: var

A key that indicates the cumulative elevation ascended during a workout.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
let HKMetadataKeyElevationAscended: String
```

#### Discussion

Set this key on  a workout, workout segment, or a quantity sample that represents distance. Set its value to an [`HKQuantity`](hkquantity.md) object with a length unit.

HealthKit assigns this metadata key to the segments it automatically creates for [`HKWorkoutActivityType.downhillSkiing`](hkworkoutactivitytype/downhillskiing.md) and [`HKWorkoutActivityType.snowboarding`](hkworkoutactivitytype/snowboarding.md) workout sessions (Apple Watch Series 3 only).

## See Also

- [let HKMetadataKeyAlpineSlopeGrade: String](hkmetadatakeyalpineslopegrade.md)
  A key that indicates the percent slope of a ski run.
- [let HKMetadataKeyElevationDescended: String](hkmetadatakeyelevationdescended.md)
  A key that indicates the cumulative elevation descended during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyelevationascended)*