# HKActivityMoveMode

**Framework**: HealthKit  
**Kind**: enum

Constants that specify the value measured by the Move ring on the user’s device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum HKActivityMoveMode
```

#### Overview

For younger users, HealthKit’s activity summary can track move time instead of active energy burned:

- HealthKit encourages users under 13 years old to track move time.
- Users 13 to 18 years old can choose to track move time or active energy burned.
- All users over 18 years old track active energy burned.

## Topics

### Move Modes
- [HKActivityMoveMode.activeEnergy](hkactivitymovemode/activeenergy.md)
  A value that indicates the Move ring measures active energy burned.
- [HKActivityMoveMode.appleMoveTime](hkactivitymovemode/applemovetime.md)
  A value that indicates the Activity app’s Move ring measures Apple Move Time.
### Initializers
- [init?(rawValue: Int)](hkactivitymovemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var activityMoveMode: HKActivityMoveMode](hkactivitysummary/activitymovemode.md)
  The move mode that they system used for this activity summary.
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
- [enum HKCategoryValueAppleStandHour](hkcategoryvalueapplestandhour.md)
  Categories that the system used to indicate whether the user stood during the sample’s duration.
- [func dateComponents(for: Calendar) -> DateComponents](hkactivitysummary/datecomponents(for:).md)
  Date components that uniquely identify the day represented by the summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitymovemode)*