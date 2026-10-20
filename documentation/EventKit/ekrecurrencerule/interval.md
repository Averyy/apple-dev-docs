# interval

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

Specifies how often the recurrence rule repeats over the unit of time indicated by its frequency.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var interval: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger interval;
```

#### Discussion

For example, a recurrence rule with a frequency type of [`EKRecurrenceFrequency.weekly`](../ekrecurrencefrequency/weekly.md) and an interval of `2` repeats every two weeks.

## See Also

### Accessing Recurrence Rule Properties
- [enum EKRecurrenceFrequency](../ekrecurrencefrequency.md)
  The frequency for recurrence rules.
- [var calendarIdentifier: String](./calendaridentifier.md)
  The identifier for the recurrence rule’s calendar.
- [var recurrenceEnd: EKRecurrenceEnd?](./recurrenceend.md)
  Indicates when the recurrence rule ends.
- [var frequency: EKRecurrenceFrequency](./frequency.md)
  The frequency of the recurrence rule.
- [var firstDayOfTheWeek: Int](./firstdayoftheweek.md)
  Indicates which day of the week the recurrence rule treats as the first day of the week.
- [var daysOfTheWeek: [EKRecurrenceDayOfWeek]?](./daysoftheweek.md)
  The days of the week associated with the recurrence rule, as an array of [`EKRecurrenceDayOfWeek`](../ekrecurrencedayofweek.md) objects.
- [var daysOfTheMonth: [NSNumber]?](./daysofthemonth.md)
  The days of the month associated with the recurrence rule, as an array of `NSNumber` objects.
- [var daysOfTheYear: [NSNumber]?](./daysoftheyear.md)
  The days of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var weeksOfTheYear: [NSNumber]?](./weeksoftheyear.md)
  The weeks of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var monthsOfTheYear: [NSNumber]?](./monthsoftheyear.md)
  The months of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var setPositions: [NSNumber]?](./setpositions.md)
  An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency.
- [func EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()](../ek_lose_fractional_seconds_do_not_use%28%29.md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/interval)*