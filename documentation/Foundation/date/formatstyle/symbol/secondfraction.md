# Date.FormatStyle.Symbol.SecondFraction

**Framework**: Foundation  
**Kind**: struct

A type that specifies the format for the second fraction in a date format style.

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
struct SecondFraction
```

#### Overview

The type [`Date.FormatStyle.Symbol.SecondFraction`](date/formatstyle/symbol/secondfraction.md) includes static factory methods that create custom [`Date.FormatStyle.Symbol.SecondFraction`](date/formatstyle/symbol/secondfraction.md) objects:

| Factory variable | Description |
| --- | --- |
| [`fractional(_:)`](date/formatstyle/symbol/secondfraction/fractional(_:).md) | Returns the numerical representation of the fractional component of the second. For example, `8`, `827`. |
| [`milliseconds(_:)`](date/formatstyle/symbol/secondfraction/milliseconds(_:).md) | Returns the number of milliseconds elapsed in the day. For example, `11122827`. |

To customize the second format in a string representation of a `Date`, use [`secondFraction(_:)`](date/formatstyle/secondfraction(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.SecondFraction`](date/formatstyle/symbol/secondfraction.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05:41 PM
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(3))) // 827
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(1))) // 8
meetingDate.formatted(Date.FormatStyle().secondFraction(.milliseconds(4))) // 11122827
```

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Second Fraction
- [static func fractional(Int) -> Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction/fractional(_:).md)
  Creates a custom format style representing the fractional seconds component of a date.
- [static func milliseconds(Int) -> Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction/milliseconds(_:).md)
  Creates a custom format style representing the milliseconds elapsed in a day.
### Comparing Second Fractions
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction/omitted.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/secondfraction)*