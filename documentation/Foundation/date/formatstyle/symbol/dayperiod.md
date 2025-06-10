# Date.FormatStyle.Symbol.DayPeriod

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for the time period in a date format style.

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
struct DayPeriod
```

#### Overview

The type [`Date.FormatStyle.Symbol.DayPeriod`](date/formatstyle/symbol/dayperiod.md) includes static factory methods that create custom [`Date.FormatStyle.Symbol.DayPeriod`](date/formatstyle/symbol/dayperiod.md) objects.

| Factory variable | Description |
| --- | --- |
| [`conversational(_:)`](date/formatstyle/symbol/dayperiod/conversational(_:).md) | Conversational abbreviated period. For example, `at night`, `nachm.`, `iltap`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Conversational narrow period. For example, `at night`, `nachmittags`, `iltapäivällä`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Conversational wide period. For example, `at night`, `nachm.`, `ip.` |
| [`standard(_:)`](date/formatstyle/symbol/dayperiod/standard(_:).md) | Abbreviated period. For example, `am`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Narrow period. For example, `a`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Wide period. For example, `am`. |
| [`with12s(_:)`](date/formatstyle/symbol/dayperiod/with12s(_:).md) | Abbreviated period including designations for noon and midnight. For example, `mid.` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Narrow period including designations for noon and midnight. For example, `md`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Wide period including designations for noon and midnight. For example, `midnight`. |

The day period format style may be uppercase or lowercase depending on the locale and other options.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Day Period
- [static func conversational(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/conversational(_:).md)
  Static factory method that creates a custom day period format style using a conversational style.
- [static func standard(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/standard(_:).md)
  Static factory method that creates a custom day period format style using a standard style.
- [static func with12s(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/with12s(_:).md)
  Static factory method that creates a custom day period format style using a style that represents midday and midnight.
### Supporting Enumerations
- [Date.FormatStyle.Symbol.DayPeriod.Width](date/formatstyle/symbol/dayperiod/width.md)
  A type representing the width of a day period in a format style.
### Comparing Day Periods
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/omitted.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod)*