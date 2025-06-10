# Date.FormatStyle.Symbol.Month

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for the month in a date format style.

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
struct Month
```

#### Overview

The type [`Date.FormatStyle.Symbol.Month`](date/formatstyle/symbol/month.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Month`](date/formatstyle/symbol/month.md) objects:

| Factory variable | Description |
| --- | --- |
| [`abbreviated`](date/formatstyle/symbol/month/abbreviated.md) | Abbreviated month name. For example, `Sep`. |
| [`defaultDigits`](date/formatstyle/symbol/month/defaultdigits.md) | Minimum number of digits that represents the numeric month. For example, `9`, `12`. |
| [`narrow`](date/formatstyle/symbol/month/narrow.md) | Narrow month name. For example, `S`. |
| [`twoDigits`](date/formatstyle/symbol/month/twodigits.md) | Two-digit numeric month, zero-padded if necessary. For example, `09`, `12`. |
| [`wide`](date/formatstyle/symbol/month/wide.md) | Wide month name. For example, `September`. |

To customize the month format in a string representation of a `Date`, use [`month(_:)`](date/formatstyle/month(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Month`](date/formatstyle/symbol/month.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().month(.abbreviated)) // Feb
meetingDate.formatted(Date.FormatStyle().month(.narrow)) // F
meetingDate.formatted(Date.FormatStyle().month(.defaultDigits)) // 2
meetingDate.formatted(Date.FormatStyle().month(.twoDigits)) // 02
meetingDate.formatted(Date.FormatStyle().month(.wide)) // February
meetingDate.formatted(Date.FormatStyle().month()) // Feb
```

If no format is specified as a parameter, the [`abbreviated`](date/formatstyle/symbol/month/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Month
- [static var abbreviated: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/abbreviated.md)
  The abbreviated representation of a month.
- [static var defaultDigits: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/defaultdigits.md)
  Custom month format style showing the minimum number of digits that represents the numeric month.
- [static var narrow: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/narrow.md)
  The shortest representation of a month.
- [static var twoDigits: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/twodigits.md)
  The custom month format style that uses two digits to represent the numeric month.
- [static var wide: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/wide.md)
  The full representation of a month.
### Comparing a Month
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month/omitted.md)

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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/month)*