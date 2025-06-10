# Date.FormatStyle.Symbol.Day

**Framework**: Foundation  
**Kind**: struct

A type that specifies the format for a day in a date format style.

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
struct Day
```

#### Overview

The [`Date.FormatStyle.Symbol.Day`](date/formatstyle/symbol/day.md) type includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.Day`](date/formatstyle/symbol/day.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](date/formatstyle/symbol/day/defaultdigits.md) | The minimum number of digits that shows the numeric day of month. For example, `1`, `18`. |
| [`julianModified(minimumLength:)`](date/formatstyle/symbol/day/julianmodified(minimumlength:).md) | The modified Julian day. The field length specifies the minimum number of digits, zero-padded if necessary. For example, `2451334`. |
| [`ordinalOfDayInMonth`](date/formatstyle/symbol/day/ordinalofdayinmonth.md) | The ordinal of the day in the month. For example, the second Wednesday in July would yield `2`. |
| [`twoDigits`](date/formatstyle/symbol/day/twodigits.md) | The two-digit numeric day of month, zero-padded if necessary. For example, `01`, `18`. |

To customize the day format in a string representation of a `Date`, use [`day(_:)`](date/formatstyle/day(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Day`](date/formatstyle/symbol/day.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().day(.defaultDigits)) // 9
meetingDate.formatted(Date.FormatStyle().day(.ordinalOfDayInMonth)) // 2 (second Tuesday of the month)
meetingDate.formatted(Date.FormatStyle().day(.twoDigits)) // 09
meetingDate.formatted(Date.FormatStyle().day(.julianModified(minimumLength: 12))) // 0002459255
meetingDate.formatted(Date.FormatStyle().day()) // 9
```

If no format is specified as a parameter, the [`defaultDigits`](date/formatstyle/symbol/day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Day Format
- [static var defaultDigits: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/defaultdigits.md)
  Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [static var ordinalOfDayInMonth: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/ordinalofdayinmonth.md)
  Custom format style portraying the ordinal of the day in the month.
- [static var twoDigits: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/twodigits.md)
  Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.
- [static func julianModified(minimumLength: Int) -> Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/julianmodified(minimumlength:).md)
  Creates a custom day format style representing the modified Julian day.
### Comparing Day Formats
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/omitted.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear.md)
  A type that specifies a format for a cyclic year in a date format style.
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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day)*