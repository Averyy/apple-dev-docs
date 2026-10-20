# appleExerciseTimeGoal

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The user’s daily exercise goal.

**Availability**:
- iOS 9.3+ - Deprecated in 27.2
- iPadOS 9.3+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.2+ - Deprecated in 27.2

## Declaration

```swift
var appleExerciseTimeGoal: HKQuantity { get set }
```

```objc
@property (nonatomic, strong) HKQuantity * appleExerciseTimeGoal;
```

#### Discussion

The [`HKQuantity`](../hkquantity.md) object for this property must use time units.

## See Also

### Related Documentation
- [static let appleExerciseTime: HKQuantityTypeIdentifier](../hkquantitytypeidentifier/appleexercisetime.md)
  A quantity sample type that measures the amount of time the user spent exercising.
### Accessing the summary’s data
- [var activityMoveMode: HKActivityMoveMode](./activitymovemode.md)
  The move mode that they system used for this activity summary.
- [enum HKActivityMoveMode](../hkactivitymovemode.md)
  Constants that specify the value measured by the Move ring on the user’s device.
- [var activeEnergyBurned: HKQuantity](./activeenergyburned.md)
  The amount of active energy the user burned during the specified day.
- [var activeEnergyBurnedGoal: HKQuantity](./activeenergyburnedgoal.md)
  The user’s daily goal for active energy burned.
- [var appleMoveTime: HKQuantity](./applemovetime.md)
  The amount of time the user spent performing activities that involve full-body movements during the specified day.
- [var appleMoveTimeGoal: HKQuantity](./applemovetimegoal.md)
  The user’s daily goal for move time.
- [var appleExerciseTime: HKQuantity](./appleexercisetime.md)
  The amount of time that the user has spent exercising during the specified day.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummary/appleexercisetimegoal)*