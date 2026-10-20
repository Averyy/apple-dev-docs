# week(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified week format style.

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
func week(_ format: Date.FormatStyle.Symbol.Week = .defaultDigits) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified week format style.

#### Discussion

Possible values of [`Date.FormatStyle.Symbol.Week`](./symbol/week.md) include [`defaultDigits`](./symbol/week/defaultdigits.md), [`twoDigits`](./symbol/week/twodigits.md), and [`weekOfMonth`](./symbol/week/weekofmonth.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Week`](./symbol/week.md) format styles applied to a date:

```swift
let meetingDate = Date() // May 3, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().week(.defaultDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.twoDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.weekOfMonth)) // 2
meetingDate.formatted(Date.FormatStyle().week()) // 19

```

An incomplete week at the start of a month is the first week of the month `1`. If you don’t provide a format, the [`defaultDigits`](./symbol/week/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](../formatstyle.md).

## Parameters

- `format`: The week format style applied to the date format style.

## See Also

### Specifying the Date Format
- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle](./day%28_%29.md)
  Modifies the date format style to use the specified day format style.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle](./dayofyear%28_%29.md)
  Modifies the date format style to use the specified day of the year format style.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle](./era%28_%29.md)
  Modifies the date format style to use the specified era format style.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle](./month%28_%29.md)
  Modifies the date format style to use the specified month format style.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle](./quarter%28_%29.md)
  Modifies the date format style to use the specified quarter format style.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](./weekday%28_%29.md)
  Modifies the date format style to use the specified weekday format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](./year%28_%29.md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](./datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/week(_:))*