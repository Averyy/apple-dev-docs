# HKWorkoutSessionLocationType

**Framework**: HealthKit  
**Kind**: enum

A constant indicating whether the workout session takes place indoors or outdoors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKWorkoutSessionLocationType
```

## Topics

### Constants
- [HKWorkoutSessionLocationType.unknown](hkworkoutsessionlocationtype/unknown.md)
  It is not known whether the workout session is taking place indoors or outdoors.
- [HKWorkoutSessionLocationType.indoor](hkworkoutsessionlocationtype/indoor.md)
  The workout session is indoors.
- [HKWorkoutSessionLocationType.outdoor](hkworkoutsessionlocationtype/outdoor.md)
  The workout session is outdoors.
### Initializers
- [init?(rawValue: Int)](hkworkoutsessionlocationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var activityType: HKWorkoutActivityType](hkworkoutconfiguration/activitytype.md)
  The workout session’s activity type.
- [var locationType: HKWorkoutSessionLocationType](hkworkoutconfiguration/locationtype.md)
  The workout session’s location.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](hkworkoutconfiguration/swimminglocationtype.md)
  The workout session’s swimming location.
- [enum HKWorkoutSwimmingLocationType](hkworkoutswimminglocationtype.md)
  The possible locations for swimming.
- [var lapLength: HKQuantity?](hkworkoutconfiguration/laplength.md)
  The length of the lap for a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype)*