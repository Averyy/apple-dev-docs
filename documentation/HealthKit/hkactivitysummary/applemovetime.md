# appleMoveTime

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The amount of time the user spent performing activities that involve full-body movements during the specified day.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var appleMoveTime: HKQuantity { get set }
```

```objc
@property (nonatomic, strong) HKQuantity * appleMoveTime;
```

## Discussion

Move time measures every full minute where the watch detects active, full-body movements, like walking, running, or playing in the playground. For younger users, HealthKit’s activity summary can track move time instead of active energy burned. For more information, see [`HKActivityMoveMode.appleMoveTime`](../hkactivitymovemode/applemovetime.md).

The [`HKQuantity`](../hkquantity.md) object for this property must use units of time, such as [`hour()`](../hkunit/hour%28%29.md), [`minute()`](../hkunit/minute%28%29.md), or [`second()`](../hkunit/second%28%29.md).

## See Also

### Accessing the summary’s data
- [var activityMoveMode: HKActivityMoveMode](./activitymovemode.md)
  The move mode that they system used for this activity summary.
- [enum HKActivityMoveMode](../hkactivitymovemode.md)
  Constants that specify the value measured by the Move ring on the user’s device.
- [var activeEnergyBurned: HKQuantity](./activeenergyburned.md)
  The amount of active energy the user burned during the specified day.
- [var activeEnergyBurnedGoal: HKQuantity](./activeenergyburnedgoal.md)
  The user’s daily goal for active energy burned.
- [var appleMoveTimeGoal: HKQuantity](./applemovetimegoal.md)
  The user’s daily goal for move time.
- [var appleExerciseTime: HKQuantity](./appleexercisetime.md)
  The amount of time that the user has spent exercising during the specified day.
- [var appleExerciseTimeGoal: HKQuantity](./appleexercisetimegoal.md)
  The user’s daily exercise goal.
- [var exerciseTimeGoal: HKQuantity?](./exercisetimegoal.md)
  The user’s daily goal for exercise time.
- [var appleStandHours: HKQuantity](./applestandhours.md)
  The number hours in the specified day during which the user has stood and moved for at least a minute per hour.
- [var standHoursGoal: HKQuantity?](./standhoursgoal.md)
  The user’s daily goal for stand hours.
- [var appleStandHoursGoal: HKQuantity](./applestandhoursgoal.md)
  The user’s daily goal for stand hours.
- [enum HKCategoryValueAppleStandHour](../hkcategoryvalueapplestandhour.md)
  Categories that the system used to indicate whether the user stood during the sample’s duration.
- [func dateComponents(for: Calendar) -> DateComponents](./datecomponents%28for%29.md)
  Date components that uniquely identify the day represented by the summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummary/applemovetime)*