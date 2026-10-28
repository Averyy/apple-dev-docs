# appleExerciseTime

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The amount of time that the user has spent exercising during the specified day.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
var appleExerciseTime: HKQuantity { get set }
```

```objc
@property (nonatomic, strong) HKQuantity * appleExerciseTime;
```

## Discussion

Exercise time measures every full minute of movement that equals or exceeds the intensity of a brisk walk.

Apple watch automatically records exercise time. By default, the watch uses the accelerometer to estimate the intensity of the user’s movement. However, during workout sessions, the watch uses additional sensors, like the heart rate sensor and GPS, to generate estimates. [`HKWorkoutSession`](../hkworkoutsession.md) sessions also contribute to the exercise time.  For more information, see [Fill the Activity rings](../hkworkout.md#Fill-the-Activity-rings).

The [`HKQuantity`](../hkquantity.md) object for this property must use units of time, such as [`hour()`](../hkunit/hour%28%29.md), [`minute()`](../hkunit/minute%28%29.md), or [`second()`](../hkunit/second%28%29.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummary/appleexercisetime)*