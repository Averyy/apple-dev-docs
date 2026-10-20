# Date.FormatStyle.Symbol.DayOfYear

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that specifies the format for the day of the year in a date format style.

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
struct DayOfYear
```

#### Overview

The type [`Date.FormatStyle.Symbol.DayOfYear`](./dayofyear.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.DayOfYear`](./dayofyear.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](./dayofyear/defaultdigits.md) | The minimum number of digits that represents the full day of the year. For example, `1`, `18`, `317`. |
| [`threeDigits`](./dayofyear/threedigits.md) | Three-digit numeric day of the year, zero-padded if necessary. For example, `001`, `018`, `317`. |
| [`twoDigits`](./dayofyear/twodigits.md) | Two-digit numeric day of the year, zero-padded if necessary. This format has no effect on three-digit values. For example, `01`, `18`, `317`. |

To customize the day format in a string representation of a `Date`, use [`dayOfYear(_:)`](../dayofyear%28_%29.md). The following example shows a variety of [`Date.FormatStyle.Symbol.DayOfYear`](./dayofyear.md) formats applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().dayOfYear(.defaultDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.twoDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.threeDigits)) // 040
meetingDate.formatted(Date.FormatStyle().dayOfYear()) // 40

```

If no format is specified as a parameter, the [`defaultDigits`](./dayofyear/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Day of Year Value
- [static var defaultDigits: Date.FormatStyle.Symbol.DayOfYear](./dayofyear/defaultdigits.md)
  Custom format style portraying the minimum number of digits that represents the numeric day of the year.
- [static var threeDigits: Date.FormatStyle.Symbol.DayOfYear](./dayofyear/threedigits.md)
  Custom format style portraying the three-digit numeric day of the year, zero-padded if necessary.
- [static var twoDigits: Date.FormatStyle.Symbol.DayOfYear](./dayofyear/twodigits.md)
  Custom format style portraying the two-digit numeric day of the year, zero-padded if necessary.
### Comparing Day of Year Values
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.DayOfYear](./dayofyear/omitted.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayofyear)*