# Date.FormatStyle.Symbol.CyclicYear

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for a cyclic year in a date format style.

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
struct CyclicYear
```

#### Overview

Calendars such as the Chinese lunar calendar and Hindu calendars use 60-year cycles of year names. If the calendar doesn’t provide cyclic year-name data, or if the year value to format is out of the range of years for which the system provides cyclic name data, then the formatting is numeric, as in [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md).

The [`Date.FormatStyle.Symbol.CyclicYear`](date/formatstyle/symbol/cyclicyear.md) type includes static factory variables that create custom [`Date.FormatStyle.Symbol.CyclicYear`](date/formatstyle/symbol/cyclicyear.md) objects:

| Factory variable | Description |
| --- | --- |
| [`abbreviated`](date/formatstyle/symbol/cyclicyear/abbreviated.md) | A shortened representation of the cyclic year appropriate for space-constrained applications. |
| [`narrow`](date/formatstyle/symbol/cyclicyear/narrow.md) | The shortest representation of the cyclic year. |
| [`wide`](date/formatstyle/symbol/cyclicyear/wide.md) | The full representation of the cyclic year. |

If no format is specified as a parameter, the [`abbreviated`](date/formatstyle/symbol/cyclicyear/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Cyclic Year
- [static var abbreviated: Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear/abbreviated.md)
  Custom cyclic year format style that portrays a shortened cyclic year.
- [static var narrow: Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear/narrow.md)
  Custom cyclic year format style that portrays the shortest representation of a cyclic year.
- [static var wide: Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear/wide.md)
  Custom cyclic year format style that portrays a complete representation of a cyclic year.
### Comparing Cyclic Years
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear/omitted.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/cyclicyear)*