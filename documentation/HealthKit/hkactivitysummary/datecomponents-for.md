# dateComponents(for:)

**Framework**: HealthKit  
**Kind**: method

Date components that uniquely identify the day represented by the summary object.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
func dateComponents(for calendar: Calendar) -> DateComponents
```

#### Return Value

Date components that uniquely specify a day. For example, for the Gregorian calendar, the date components consist of only the era, year, month, and day.

#### Discussion

Each activity summary covers a single day. The day always begins and ends at midnight; however, the day may be longer or shorter than 24 hours (for example, if the user traveled across time zones).

## Parameters

- `calendar`: The calendar used to calculate the date components.

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
- [enum HKCategoryValueAppleStandHour](hkcategoryvalueapplestandhour.md)
  Categories that the system used to indicate whether the user stood during the sample’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummary/datecomponents(for:))*