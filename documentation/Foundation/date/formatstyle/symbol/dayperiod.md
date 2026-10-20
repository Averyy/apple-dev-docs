# Date.FormatStyle.Symbol.DayPeriod

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

The type [`Date.FormatStyle.Symbol.DayPeriod`](./dayperiod.md) includes static factory methods that create custom [`Date.FormatStyle.Symbol.DayPeriod`](./dayperiod.md) objects.

| Factory variable | Description |
| --- | --- |
| [`conversational(_:)`](./dayperiod/conversational%28_%29.md) | Conversational abbreviated period. For example, `at night`, `nachm.`, `iltap`. ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Conversational narrow period. For example, `at night`, `nachmittags`, `iltapäivällä`. ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Conversational wide period. For example, `at night`, `nachm.`, `ip.` |
| [`standard(_:)`](./dayperiod/standard%28_%29.md) | Abbreviated period. For example, `am`. ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Narrow period. For example, `a`. ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Wide period. For example, `am`. |
| [`with12s(_:)`](./dayperiod/with12s%28_%29.md) | Abbreviated period including designations for noon and midnight. For example, `mid.` ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Narrow period including designations for noon and midnight. For example, `md`. ![](https://developer.apple.com/tutorials/images/com.apple.foundation/spacer.png) Wide period including designations for noon and midnight. For example, `midnight`. |

The day period format style may be uppercase or lowercase depending on the locale and other options.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Day Period
- [static func conversational(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](./dayperiod/conversational%28_%29.md)
  Static factory method that creates a custom day period format style using a conversational style.
- [static func standard(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](./dayperiod/standard%28_%29.md)
  Static factory method that creates a custom day period format style using a standard style.
- [static func with12s(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](./dayperiod/with12s%28_%29.md)
  Static factory method that creates a custom day period format style using a style that represents midday and midnight.
### Supporting Enumerations
- [Date.FormatStyle.Symbol.DayPeriod.Width](./dayperiod/width.md)
  A type representing the width of a day period in a format style.
### Comparing Day Periods
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.DayPeriod](./dayperiod/omitted.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod)*