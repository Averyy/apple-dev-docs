# EKRecurrenceRule

**Framework**: Eventkit  
**Kind**: class

A class that describes the pattern for a recurring event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKRecurrenceRule
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)

#### Overview

After you create a recurrence rule, assign it to an event with the method of [`EKEvent`](ekevent.md).

Recurrence rules can have an end, represented by an [`EKRecurrenceEnd`](ekrecurrenceend.md) object. The end can be based on a specific date or a maximum number of occurrences.

> **Note**:  It is currently not possible to directly modify an `EKRecurrenceRule` or any of its properties. This functionality is achieved by creating a new `EKRecurrenceRule` and setting an event or reminder to use the newly created rule.

## Topics

### Creating a Basic Recurrence Rule
- [enum EKSpan](ekspan.md)
  An object that indicates whether modifications should apply to a single event or all future events of a recurring event.
- [init(recurrenceWith: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)](ekrecurrencerule/init(recurrencewith:interval:end:).md)
  Initializes and returns a simple recurrence rule with a given frequency, interval, and end.
### Creating a Complex Recurrence Rule
- [init(recurrenceWith: EKRecurrenceFrequency, interval: Int, daysOfTheWeek: [EKRecurrenceDayOfWeek]?, daysOfTheMonth: [NSNumber]?, monthsOfTheYear: [NSNumber]?, weeksOfTheYear: [NSNumber]?, daysOfTheYear: [NSNumber]?, setPositions: [NSNumber]?, end: EKRecurrenceEnd?)](ekrecurrencerule/init(recurrencewith:interval:daysoftheweek:daysofthemonth:monthsoftheyear:weeksoftheyear:daysoftheyear:setpositions:end:).md)
  Initializes and returns a recurrence rule with a given frequency and additional scheduling information.
### Accessing Recurrence Rule Properties
- [enum EKRecurrenceFrequency](ekrecurrencefrequency.md)
  The frequency for recurrence rules.
- [var calendarIdentifier: String](ekrecurrencerule/calendaridentifier.md)
  The identifier for the recurrence rule’s calendar.
- [var recurrenceEnd: EKRecurrenceEnd?](ekrecurrencerule/recurrenceend.md)
  Indicates when the recurrence rule ends.
- [var frequency: EKRecurrenceFrequency](ekrecurrencerule/frequency.md)
  The frequency of the recurrence rule.
- [var interval: Int](ekrecurrencerule/interval.md)
  Specifies how often the recurrence rule repeats over the unit of time indicated by its frequency.
- [var firstDayOfTheWeek: Int](ekrecurrencerule/firstdayoftheweek.md)
  Indicates which day of the week the recurrence rule treats as the first day of the week.
- [var daysOfTheWeek: [EKRecurrenceDayOfWeek]?](ekrecurrencerule/daysoftheweek.md)
  The days of the week associated with the recurrence rule, as an array of [`EKRecurrenceDayOfWeek`](ekrecurrencedayofweek.md) objects.
- [var daysOfTheMonth: [NSNumber]?](ekrecurrencerule/daysofthemonth.md)
  The days of the month associated with the recurrence rule, as an array of `NSNumber` objects.
- [var daysOfTheYear: [NSNumber]?](ekrecurrencerule/daysoftheyear.md)
  The days of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var weeksOfTheYear: [NSNumber]?](ekrecurrencerule/weeksoftheyear.md)
  The weeks of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var monthsOfTheYear: [NSNumber]?](ekrecurrencerule/monthsoftheyear.md)
  The months of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var setPositions: [NSNumber]?](ekrecurrencerule/setpositions.md)
  An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency.
- [func EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()](ek_lose_fractional_seconds_do_not_use().md)
  A deprecated function.

## Relationships

### Inherits From
- [EKObject](ekobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating a recurring event](creating-a-recurring-event.md)
  Set up an event or reminder that repeats.
- [class EKRecurrenceDayOfWeek](ekrecurrencedayofweek.md)
  A class that represents the day of the week.
- [class EKRecurrenceEnd](ekrecurrenceend.md)
  A class that defines the end of a recurrence rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/EventKit/ekrecurrencerule)*