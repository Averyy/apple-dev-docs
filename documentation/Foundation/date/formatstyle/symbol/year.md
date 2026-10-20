# Date.FormatStyle.Symbol.Year

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

The [`Date.FormatStyle.Symbol.Year`](./year.md) type includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.Year`](./year.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](./year/defaultdigits.md) | The minimum number of digits that represents the full year. For example, `2`, `20`, `201`, `2017`. |
| [`twoDigits`](./year/twodigits.md) | The year’s two lowest-order digits, zero-padded or truncated if necessary. For example, `02`, `20`, `01`, `17`, `73`. |
| [`padded(_:)`](./year/padded%28_%29.md) | Three or more digits, zero-padded if necessary. For example, `002`, `020`, `201`, `2017`. |
| [`relatedGregorian(minimumLength:)`](./year/relatedgregorian%28minimumlength%29.md) | For non-Gregorian calendars, output corresponds to the extended Gregorian year in which the calendar’s year begins. The default length is the minimum needed to show the full year. |
| [`extended(minimumLength:)`](./year/extended%28minimumlength%29.md) | A single number designating the year of the calendar system, encompassing all supra-year fields. The default length is the minimum needed to show the full year. |

To customize the year format in a string representation of a `Date`, use [`year(_:)`](../year%28_%29.md). The following example shows a variety of [`Date.FormatStyle.Symbol.Year`](./year.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().year(.defaultDigits)) // 2021
meetingDate.formatted(Date.FormatStyle().year(.twoDigits)) // 21
meetingDate.formatted(Date.FormatStyle().year(.extended(minimumLength: 5))) // 02021
meetingDate.formatted(Date.FormatStyle().year(.extended())) // 2021
meetingDate.formatted(Date.FormatStyle().year(.padded(6))) // 002021
meetingDate.formatted(Date.FormatStyle().year(.relatedGregorian())) // 2021
```

If no format is specified as a parameter, the [`defaultDigits`](./day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Year
- [static var defaultDigits: Date.FormatStyle.Symbol.Year](./year/defaultdigits.md)
  The custom year format style showing the minimum number of digits that represents the numeric year.
- [static var twoDigits: Date.FormatStyle.Symbol.Year](./year/twodigits.md)
  The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [static func padded(Int) -> Date.FormatStyle.Symbol.Year](./year/padded%28_%29.md)
  Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [static func relatedGregorian(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](./year/relatedgregorian%28minimumlength%29.md)
  Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [static func extended(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](./year/extended%28minimumlength%29.md)
  Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.
### Comparing Years
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Year](./year/omitted.md)
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
- [Date.FormatStyle.Symbol.Day](./day.md)
  A type that specifies the format for a day in a date format style.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year)*