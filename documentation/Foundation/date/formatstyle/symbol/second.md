# Date.FormatStyle.Symbol.Second

**Framework**: Foundation  
**Kind**: struct

A type that specifies the format for the seconds in a date format style.

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
struct Second
```

#### Overview

The type [`Date.FormatStyle.Symbol.Second`](date/formatstyle/symbol/second.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Second`](date/formatstyle/symbol/second.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](date/formatstyle/symbol/second/defaultdigits.md) | The minimum number of digits that represents the numeric second. For example, `1`, `18`. |
| [`twoDigits`](date/formatstyle/symbol/second/twodigits.md) | Two-digit numeric second, zero-padded if necessary. For example, `01`, `18`. |

To customize the second format in a string representation of a `Date`, use [`second(_:)`](date/formatstyle/second(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Second`](date/formatstyle/symbol/second.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().second(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().second(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().second()) // 5
```

If no format is specified as a parameter, the [`defaultDigits`](date/formatstyle/symbol/second/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Second
- [static var defaultDigits: Date.FormatStyle.Symbol.Second](date/formatstyle/symbol/second/defaultdigits.md)
  The custom format style that conveys the minimum number of digits that represents the numeric second.
- [static var twoDigits: Date.FormatStyle.Symbol.Second](date/formatstyle/symbol/second/twodigits.md)
  The custom format style that conveys a two-digit numeric second, zero-padded if necessary.
### Comparing Seconds
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Second](date/formatstyle/symbol/second/omitted.md)

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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/second)*