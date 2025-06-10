# HKActivitySummary

**Framework**: HealthKit  
**Kind**: class

An object that contains the move, exercise, and stand data for a given day.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
class HKActivitySummary
```

## Mentions

- [Executing Activity Summary Queries](executing-activity-summary-queries.md)

#### Overview

You can read [`HKActivitySummary`](hkactivitysummary.md) objects from the HealthKit store using an [`HKActivitySummaryQuery`](hkactivitysummaryquery.md) object. Unlike the [`HKSample`](hksample.md) subclasses,  [`HKActivitySummary`](hkactivitysummary.md) instances are mutable, but changes made to the object’s properties have no affect on the values in the HealthKit store.

You can instantiate your own [`HKActivitySummary`](hkactivitysummary.md) objects (if needed), but you can’t save [`HKActivitySummary`](hkactivitysummary.md) objects to the store.

You can display an active summary in iOS using the [`HKActivityRingView`](https://developer.apple.com/documentation/healthkitui/hkactivityringview) class or in watchOS using the [`WKInterfaceActivityRing`](https://developer.apple.com/documentation/WatchKit/WKInterfaceActivityRing) class.

## Topics

### Accessing the summary’s data
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
- [func dateComponents(for: Calendar) -> DateComponents](hkactivitysummary/datecomponents(for:).md)
  Date components that uniquely identify the day represented by the summary object.
### Specifying predicate key paths
- [let HKPredicateKeyPathDateComponents: String](hkpredicatekeypathdatecomponents.md)
  The key path for accessing an activity summary’s date components.
### Instance Properties
- [var isPaused: Bool](hkactivitysummary/ispaused.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
  A query interface that reads activity summaries using Swift concurrency.
- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [class HKActivityRingView](../healthkitui/hkactivityringview.md)
  A view that uses the Move, Exercise, and Stand activity rings to display data from a HealthKit activity summary object.
- [class HKActivityMoveModeObject](hkactivitymovemodeobject.md)
  An object that contains a movement mode value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummary)*