# Date.FormatStyle.Symbol.VerbatimHour

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for the hour in a date format style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct VerbatimHour
```

## Topics

### Modifying a Verbatim Hour
- [static func defaultDigits(clock: Date.FormatStyle.Symbol.VerbatimHour.Clock, hourCycle: Date.FormatStyle.Symbol.VerbatimHour.HourCycle) -> Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour/defaultdigits(clock:hourcycle:).md)
  Creates a custom format style portraying the minimum number of digits that represents the hour.
- [static func twoDigits(clock: Date.FormatStyle.Symbol.VerbatimHour.Clock, hourCycle: Date.FormatStyle.Symbol.VerbatimHour.HourCycle) -> Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour/twodigits(clock:hourcycle:).md)
  Creates a custom format style portraying two digits that represent the hour.
### Supporting Structures
- [Date.FormatStyle.Symbol.VerbatimHour.Clock](date/formatstyle/symbol/verbatimhour/clock.md)
  A type that specifies a clock representation for the format of an hour.
- [Date.FormatStyle.Symbol.VerbatimHour.HourCycle](date/formatstyle/symbol/verbatimhour/hourcycle.md)
  A type that specifies the start of a clock representation for the format of a hour.
### Comparing a Verbatim Hour
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear.md)
  A type that specifies a format for a cyclic year in a date format style.
- [Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day.md)
  A type that specifies the format for a day in a date format style.
- [Date.FormatStyle.Symbol.DayOfYear](date/formatstyle/symbol/dayofyear.md)
  A type that specifies the format for the day of the year in a date format style.
- [Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod.md)
  A type that specifies a format for the time period in a date format style.
- [Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era.md)
  A type that specifies a format for the era in a date format style.
- [Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour.md)
  A type that specifies a format for the hour in a date format style.
- [Date.FormatStyle.Symbol.Minute](date/formatstyle/symbol/minute.md)
  A type that specifies the format for the minutes in a date format style.
- [Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month.md)
  A type that specifies a format for the month in a date format style.
- [Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter.md)
  A type that specifies the format for the quarter in a date format style.
- [Date.FormatStyle.Symbol.Second](date/formatstyle/symbol/second.md)
  A type that specifies the format for the seconds in a date format style.
- [Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction.md)
  A type that specifies the format for the second fraction in a date format style.
- [Date.FormatStyle.Symbol.StandaloneMonth](date/formatstyle/symbol/standalonemonth.md)
  A type that specifies the format for a standalone month.
- [Date.FormatStyle.Symbol.StandaloneQuarter](date/formatstyle/symbol/standalonequarter.md)
  A type that specifies the format for a standalone quarter.
- [Date.FormatStyle.Symbol.StandaloneWeekday](date/formatstyle/symbol/standaloneweekday.md)
  A type that specifies the format for a standalone weekday.
- [Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone.md)
  A type that specifies a format for the time zone in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/verbatimhour)*