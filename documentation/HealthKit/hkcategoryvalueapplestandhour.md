# HKCategoryValueAppleStandHour

**Framework**: HealthKit  
**Kind**: enum

Categories that the system used to indicate whether the user stood during the sample’s duration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKCategoryValueAppleStandHour
```

## Topics

### Constants
- [HKCategoryValueAppleStandHour.stood](hkcategoryvalueapplestandhour/stood.md)
  The user stood up and moved for at least one continuous minute during the sample.
- [HKCategoryValueAppleStandHour.idle](hkcategoryvalueapplestandhour/idle.md)
  The user didn’t stand up and move for at least one continuous minute during the sample.
### Initializers
- [init?(rawValue: Int)](hkcategoryvalueapplestandhour/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [HKCategoryValuePredicateProviding](hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activityMoveMode: HKActivityMoveMode](hkactivitysummary/activitymovemode.md)
  The move mode that they system used for this activity summary.
- [enum HKActivityMoveMode](hkactivitymovemode.md)
  Constants that specify the value measured by the Move ring on the user’s device.
- [var activeEnergyBurned: HKQuantity](hkactivitysummary/activeenergyburned.md)
  The amount of active energy the user burned during the specified day.
- [var activeEnergyBurnedGoal: HKQuantity](hkactivitysummary/activeenergyburnedgoal.md)
  The user’s daily goal for active energy burned.
- [var appleMoveTime: HKQuantity](hkactivitysummary/applemovetime.md)
  The amount of time the user spent performing activities that involve full-body movements during the specified day.
- [var appleMoveTimeGoal: HKQuantity](hkactivitysummary/applemovetimegoal.md)
  The user’s daily goal for move time.
- [var appleExerciseTime: HKQuantity](hkactivitysummary/appleexercisetime.md)
  The amount of time that the user has spent exercising during the specified day.
- [var appleExerciseTimeGoal: HKQuantity](hkactivitysummary/appleexercisetimegoal.md)
  The user’s daily exercise goal.
- [var exerciseTimeGoal: HKQuantity?](hkactivitysummary/exercisetimegoal.md)
  The user’s daily goal for exercise time.
- [var appleStandHours: HKQuantity](hkactivitysummary/applestandhours.md)
  The number hours in the specified day during which the user has stood and moved for at least a minute per hour.
- [var standHoursGoal: HKQuantity?](hkactivitysummary/standhoursgoal.md)
  The user’s daily goal for stand hours.
- [var appleStandHoursGoal: HKQuantity](hkactivitysummary/applestandhoursgoal.md)
  The user’s daily goal for stand hours.
- [func dateComponents(for: Calendar) -> DateComponents](hkactivitysummary/datecomponents(for:).md)
  Date components that uniquely identify the day represented by the summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour)*