# weeksOfTheYear

**Framework**: EventKit  
**Kind**: property

The weeks of the year associated with the recurrence rule, as an array of `NSNumber` objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var weeksOfTheYear: [NSNumber]? { get }
```

#### Discussion

Values can be from `1` to `53` and from `-1` to `-53`. This property value is valid only for recurrence rules initialized with specific weeks of the year and a frequency type of [`EKRecurrenceFrequency.yearly`](ekrecurrencefrequency/yearly.md).

Negative values indicate counting backwards from the end of the year.

## See Also

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
- [var monthsOfTheYear: [NSNumber]?](ekrecurrencerule/monthsoftheyear.md)
  The months of the year associated with the recurrence rule, as an array of `NSNumber` objects.
- [var setPositions: [NSNumber]?](ekrecurrencerule/setpositions.md)
  An array of ordinal numbers that filters which recurrences to include in the recurrence rule’s frequency.
- [func EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()](ek_lose_fractional_seconds_do_not_use().md)
  A deprecated function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/weeksoftheyear)*