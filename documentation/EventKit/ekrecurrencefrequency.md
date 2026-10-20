# EKRecurrenceFrequency

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The frequency for recurrence rules.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
enum EKRecurrenceFrequency
```

```c
enum EKRecurrenceFrequency : NSInteger;
```

## Mentions

- [Creating a recurring event](./creating-a-recurring-event.md)

## Topics

### Constants
- [EKRecurrenceFrequency.daily](./ekrecurrencefrequency/daily.md)
  Indicates a daily recurrence rule.
- [EKRecurrenceFrequency.weekly](./ekrecurrencefrequency/weekly.md)
  Indicates a weekly recurrence rule.
- [EKRecurrenceFrequency.monthly](./ekrecurrencefrequency/monthly.md)
  Indicates a monthly recurrence rule.
- [EKRecurrenceFrequency.yearly](./ekrecurrencefrequency/yearly.md)
  Indicates a yearly recurrence rule.
### Initializers
- [init?(rawValue: Int)](./ekrecurrencefrequency/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Recurrence Rule Properties
- [var calendarIdentifier: String](./ekrecurrencerule/calendaridentifier.md)
  The identifier for the recurrence rule’s calendar.
- [var recurrenceEnd: EKRecurrenceEnd?](./ekrecurrencerule/recurrenceend.md)
  Indicates when the recurrence rule ends.
- [var frequency: EKRecurrenceFrequency](./ekrecurrencerule/frequency.md)
  The frequency of the recurrence rule.
- [var interval: Int](./ekrecurrencerule/interval.md)
  Specifies how often the recurrence rule repeats over the unit of time indicated by its frequency.
- [var firstDayOfTheWeek: Int](./ekrecurrencerule/firstdayoftheweek.md)
  Indicates which day of the week the recurrence rule treats as the first day of the week.
- [var daysOfTheWeek: [EKRecurrenceDayOfWeek]?](./ekrecurrencerule/daysoftheweek.md)
  The days of the week associated with the recurrence rule, as an array of [`EKRecurrenceDayOfWeek`](./ekrecurrencedayofweek.md) objects.
- [var daysOfTheMonth: [NSNumber]?](./ekrecurrencerule/daysofthemonth.md)
  The days of the month associated with the recurrence rule, as an array of `NSNumber` objects.
- [var daysOfTheYear: [NSNumber]?](./ekrecurrencerule/daysoftheyear.md)
  The days of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var weeksOfTheYear: [NSNumber]?](./ekrecurrencerule/weeksoftheyear.md)
  The weeks of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var monthsOfTheYear: [NSNumber]?](./ekrecurrencerule/monthsoftheyear.md)
  The months of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var setPositions: [NSNumber]?](./ekrecurrencerule/setpositions.md)
  An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency.
- [func EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()](./ek_lose_fractional_seconds_do_not_use%28%29.md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencefrequency)*