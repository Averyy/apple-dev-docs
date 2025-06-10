# Date.FormatStyle.Symbol.Quarter

**Framework**: Foundation  
**Kind**: struct

A type that specifies the format for the quarter in a date format style.

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
struct Quarter
```

#### Overview

The type [`Date.FormatStyle.Symbol.Quarter`](date/formatstyle/symbol/quarter.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Quarter`](date/formatstyle/symbol/quarter.md) objects:

| Factory variable | Description |
| --- | --- |
| [`abbreviated`](date/formatstyle/symbol/quarter/abbreviated.md) | Abbreviated quarter name. For example, `Q2`. |
| [`narrow`](date/formatstyle/symbol/quarter/narrow.md) | Minimum number of digits that represents the  numeric quarter. For example, `2`. |
| [`oneDigit`](date/formatstyle/symbol/quarter/onedigit.md) | One-digit numeric quarter. For example, `1`, `4`. |
| [`twoDigits`](date/formatstyle/symbol/quarter/twodigits.md) | Two-digit numeric quarter, zero-padded if necessary. For example, `01`, `04`. |
| [`wide`](date/formatstyle/symbol/quarter/wide.md) | Wide quarter name. For example, `2nd quarter`. |

To customize the month format in a string representation of a `Date`, use [`quarter(_:)`](date/formatstyle/quarter(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Quarter`](date/formatstyle/symbol/quarter.md) format styles applied to a date.

```swift
let meetingDate = Date() // Oct 7, 2020 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().quarter(.abbreviated)) // Q4
meetingDate.formatted(Date.FormatStyle().quarter(.narrow)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter(.oneDigit)) // 4
meetingDate.formatted(Date.FormatStyle().quarter(.twoDigits)) // 04
meetingDate.formatted(Date.FormatStyle().quarter(.wide)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter()) // Q4

```

If no format is specified as a parameter, the [`abbreviated`](date/formatstyle/symbol/quarter/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Quarter
- [static var abbreviated: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/abbreviated.md)
  The abbreviated representation of a quarter.
- [static var narrow: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/narrow.md)
  The shortest representation of a quarter.
- [static var oneDigit: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/onedigit.md)
  The one-digit representation of a quarter.
- [static var twoDigits: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/twodigits.md)
  The two-digit representation of a quarter.
- [static var wide: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/wide.md)
  The full representation of a quarter.
### Comparing Quarters
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter/omitted.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/quarter)*