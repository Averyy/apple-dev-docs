# HKWorkoutSwimmingLocationType

**Framework**: HealthKit  
**Kind**: enum

The possible locations for swimming.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum HKWorkoutSwimmingLocationType
```

## Topics

### Swimming Locations
- [HKWorkoutSwimmingLocationType.openWater](hkworkoutswimminglocationtype/openwater.md)
  The user swam in open water like a lake or ocean.
- [HKWorkoutSwimmingLocationType.pool](hkworkoutswimminglocationtype/pool.md)
  The user swam in a pool.
- [HKWorkoutSwimmingLocationType.unknown](hkworkoutswimminglocationtype/unknown.md)
  The swimming location could not be determined.
### Initializers
- [init?(rawValue: Int)](hkworkoutswimminglocationtype/init(rawvalue:).md)

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
- [enum HKWorkoutSessionLocationType](hkworkoutsessionlocationtype.md)
  A constant indicating whether the workout session takes place indoors or outdoors.
- [var swimmingLocationType: HKWorkoutSwimmingLocationType](hkworkoutconfiguration/swimminglocationtype.md)
  The workout session’s swimming location.
- [var lapLength: HKQuantity?](hkworkoutconfiguration/laplength.md)
  The length of the lap for a workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype)*