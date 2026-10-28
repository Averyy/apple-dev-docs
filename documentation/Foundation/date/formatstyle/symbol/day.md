# Date.FormatStyle.Symbol.Day

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

## Overview

The [`Date.FormatStyle.Symbol.Day`](./day.md) type includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.Day`](./day.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](./day/defaultdigits.md) | The minimum number of digits that shows the numeric day of month. For example, `1`, `18`. |
| [`julianModified(minimumLength:)`](./day/julianmodified%28minimumlength%29.md) | The modified Julian day. The field length specifies the minimum number of digits, zero-padded if necessary. For example, `2451334`. |
| [`ordinalOfDayInMonth`](./day/ordinalofdayinmonth.md) | The ordinal of the day in the month. For example, the second Wednesday in July would yield `2`. |
| [`twoDigits`](./day/twodigits.md) | The two-digit numeric day of month, zero-padded if necessary. For example, `01`, `18`. |

To customize the day format in a string representation of a `Date`, use [`day(_:)`](../day%28_%29.md). The following example shows a variety of [`Date.FormatStyle.Symbol.Day`](./day.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().day(.defaultDigits)) // 9
meetingDate.formatted(Date.FormatStyle().day(.ordinalOfDayInMonth)) // 2 (second Tuesday of the month)
meetingDate.formatted(Date.FormatStyle().day(.twoDigits)) // 09
meetingDate.formatted(Date.FormatStyle().day(.julianModified(minimumLength: 12))) // 0002459255
meetingDate.formatted(Date.FormatStyle().day()) // 9
```

If no format is specified as a parameter, the [`defaultDigits`](./day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Day Format
- [static var defaultDigits: Date.FormatStyle.Symbol.Day](./day/defaultdigits.md)
  Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [static var ordinalOfDayInMonth: Date.FormatStyle.Symbol.Day](./day/ordinalofdayinmonth.md)
  Custom format style portraying the ordinal of the day in the month.
- [static var twoDigits: Date.FormatStyle.Symbol.Day](./day/twodigits.md)
  Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.
- [static func julianModified(minimumLength: Int) -> Date.FormatStyle.Symbol.Day](./day/julianmodified%28minimumlength%29.md)
  Creates a custom day format style representing the modified Julian day.
### Comparing Day Formats
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Day](./day/omitted.md)
  The option for not including the symbol in the formatted output.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Modifying Date Style Format Symbols
- [Date.FormatStyle.Symbol.CyclicYear](./cyclicyear.md)
  A type that specifies a format for a cyclic year in a date format style.
- [Date.FormatStyle.Symbol.DayOfYear](./dayofyear.md)
  A type that specifies the format for the day of the year in a date format style.
- [Date.FormatStyle.Symbol.DayPeriod](./dayperiod.md)
  A type that specifies a format for the time period in a date format style.
- [Date.FormatStyle.Symbol.Era](./era.md)
  A type that specifies a format for the era in a date format style.
- [Date.FormatStyle.Symbol.Hour](./hour.md)
  A type that specifies a format for the hour in a date format style.
- [Date.FormatStyle.Symbol.Minute](./minute.md)
  A type that specifies the format for the minutes in a date format style.
- [Date.FormatStyle.Symbol.Month](./month.md)
  A type that specifies a format for the month in a date format style.
- [Date.FormatStyle.Symbol.Quarter](./quarter.md)
  A type that specifies the format for the quarter in a date format style.
- [Date.FormatStyle.Symbol.Second](./second.md)
  A type that specifies the format for the seconds in a date format style.
- [Date.FormatStyle.Symbol.SecondFraction](./secondfraction.md)
  A type that specifies the format for the second fraction in a date format style.
- [Date.FormatStyle.Symbol.StandaloneMonth](./standalonemonth.md)
  A type that specifies the format for a standalone month.
- [Date.FormatStyle.Symbol.StandaloneQuarter](./standalonequarter.md)
  A type that specifies the format for a standalone quarter.
- [Date.FormatStyle.Symbol.StandaloneWeekday](./standaloneweekday.md)
  A type that specifies the format for a standalone weekday.
- [Date.FormatStyle.Symbol.TimeZone](./timezone.md)
  A type that specifies a format for the time zone in a date format style.
- [Date.FormatStyle.Symbol.VerbatimHour](./verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day)*