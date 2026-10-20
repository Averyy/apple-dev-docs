# Date.FormatStyle.Symbol.Week

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that specifies the format for the week in a date format style.

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
struct Week
```

#### Overview

The type [`Date.FormatStyle.Symbol.Week`](./week.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Week`](./week.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigits`](./week/defaultdigits.md) | The minimum number of digits that represents the full numeric week. For example, `1`, `18`. |
| [`twoDigits`](./week/twodigits.md) | Two-digit numeric week, zero-padded if necessary. For example, `01`, `18`. |
| [`weekOfMonth`](./week/weekofmonth.md) | The numeric week of the month. For example, `1`, `4`. |

To customize the week format in a string representation of a `Date`, use [`week(_:)`](../week%28_%29.md). The following example shows a variety of [`Date.FormatStyle.Symbol.Week`](./week.md) format styles applied to a date.

```swift
let meetingDate = Date() // May 3, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().week(.defaultDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.twoDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.weekOfMonth)) // 2
meetingDate.formatted(Date.FormatStyle().week()) // 19

```

An incomplete week at the start of a month is week of the month `1`. If no format is specified as a parameter, the [`defaultDigits`](./week/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Week
- [static var defaultDigits: Date.FormatStyle.Symbol.Week](./week/defaultdigits.md)
  Custom week format style showing the minimum number of digits that represents the numeric week.
- [static var twoDigits: Date.FormatStyle.Symbol.Week](./week/twodigits.md)
  Custom format style portraying the two-digit numeric week, zero-padded if necessary.
- [static var weekOfMonth: Date.FormatStyle.Symbol.Week](./week/weekofmonth.md)
  Custom format style portraying the numeric week of the month.
### Comparing Weeks
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Week](./week/omitted.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/week)*