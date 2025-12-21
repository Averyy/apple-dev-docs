# Date.FormatStyle.Symbol.Year

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for the year in a date format style.

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
struct Year
```

#### Overview

The [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md) type includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](date/formatstyle/symbol/year/defaultdigits.md) | The minimum number of digits that represents the full year. For example, `2`, `20`, `201`, `2017`. |
| [`twoDigits`](date/formatstyle/symbol/year/twodigits.md) | The year’s two lowest-order digits, zero-padded or truncated if necessary. For example, `02`, `20`, `01`, `17`, `73`. |
| [`padded(_:)`](date/formatstyle/symbol/year/padded(_:).md) | Three or more digits, zero-padded if necessary. For example, `002`, `020`, `201`, `2017`. |
| [`relatedGregorian(minimumLength:)`](date/formatstyle/symbol/year/relatedgregorian(minimumlength:).md) | For non-Gregorian calendars, output corresponds to the extended Gregorian year in which the calendar’s year begins. The default length is the minimum needed to show the full year. |
| [`extended(minimumLength:)`](date/formatstyle/symbol/year/extended(minimumlength:).md) | A single number designating the year of the calendar system, encompassing all supra-year fields. The default length is the minimum needed to show the full year. |

To customize the year format in a string representation of a `Date`, use [`year(_:)`](date/formatstyle/year(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().year(.defaultDigits)) // 2021
meetingDate.formatted(Date.FormatStyle().year(.twoDigits)) // 21
meetingDate.formatted(Date.FormatStyle().year(.extended(minimumLength: 5))) // 02021
meetingDate.formatted(Date.FormatStyle().year(.extended())) // 2021
meetingDate.formatted(Date.FormatStyle().year(.padded(6))) // 002021
meetingDate.formatted(Date.FormatStyle().year(.relatedGregorian())) // 2021
```

If no format is specified as a parameter, the [`defaultDigits`](date/formatstyle/symbol/day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Year
- [static var defaultDigits: Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/defaultdigits.md)
  The custom year format style showing the minimum number of digits that represents the numeric year.
- [static var twoDigits: Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/twodigits.md)
  The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [static func padded(Int) -> Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/padded(_:).md)
  Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [static func relatedGregorian(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/relatedgregorian(minimumlength:).md)
  Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [static func extended(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/extended(minimumlength:).md)
  Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.
### Comparing Years
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/omitted.md)
  The option for not including the symbol in the formatted output.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year)*