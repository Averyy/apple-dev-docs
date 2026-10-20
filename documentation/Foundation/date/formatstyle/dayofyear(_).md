# dayOfYear(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified day of the year format style.

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
func dayOfYear(_ format: Date.FormatStyle.Symbol.DayOfYear = .defaultDigits) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified day of the year style.

#### Discussion

Values of [`Date.FormatStyle.Symbol.DayOfYear`](./symbol/dayofyear.md) are [`defaultDigits`](./symbol/dayofyear/defaultdigits.md), [`threeDigits`](./symbol/dayofyear/threedigits.md), and [`twoDigits`](./symbol/dayofyear/twodigits.md).

This example shows a variety of [`Date.FormatStyle.Symbol.DayOfYear`](./symbol/dayofyear.md) formats applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().dayOfYear(.defaultDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.twoDigits)) // 40
meetingDate.formatted(Date.FormatStyle().dayOfYear(.threeDigits)) // 040
meetingDate.formatted(Date.FormatStyle().dayOfYear()) // 40

```

If you don’t provide a format, the [`defaultDigits`](./symbol/dayofyear/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](../formatstyle.md).

## Parameters

- `format`: The day of the year format style applied to the date format style.

## See Also

### Specifying the Date Format
- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle](./day%28_%29.md)
  Modifies the date format style to use the specified day format style.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle](./era%28_%29.md)
  Modifies the date format style to use the specified era format style.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle](./month%28_%29.md)
  Modifies the date format style to use the specified month format style.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle](./quarter%28_%29.md)
  Modifies the date format style to use the specified quarter format style.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](./week%28_%29.md)
  Modifies the date format style to use the specified week format style.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](./weekday%28_%29.md)
  Modifies the date format style to use the specified weekday format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](./year%28_%29.md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](./datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/dayofyear(_:))*