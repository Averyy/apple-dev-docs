# quarter(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified quarter format style.

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
func quarter(_ format: Date.FormatStyle.Symbol.Quarter = .abbreviated) -> Date.FormatStyle
```

## Return Value

A date format style modified to include the specified quarter style.

## Discussion

Possible values of [`Date.FormatStyle.Symbol.Quarter`](./symbol/quarter.md) include [`abbreviated`](./symbol/quarter/abbreviated.md), [`narrow`](./symbol/quarter/narrow.md), [`oneDigit`](./symbol/quarter/onedigit.md), [`twoDigits`](./symbol/month/twodigits.md), and [`wide`](./symbol/month/wide.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Quarter`](./symbol/quarter.md) format styles applied to a date:

```swift
let meetingDate = Date() // Oct 7, 2020 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().quarter(.abbreviated)) // Q4
meetingDate.formatted(Date.FormatStyle().quarter(.narrow)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter(.oneDigit)) // 4
meetingDate.formatted(Date.FormatStyle().quarter(.twoDigits)) // 04
meetingDate.formatted(Date.FormatStyle().quarter(.wide)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter()) // Q4

```

If you don’t provide a format, the [`abbreviated`](./symbol/quarter/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](../formatstyle.md).

## Parameters

- `format`: The quarter format style applied to the date format style.

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
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](./week%28_%29.md)
  Modifies the date format style to use the specified week format style.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](./weekday%28_%29.md)
  Modifies the date format style to use the specified weekday format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](./year%28_%29.md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](./datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/quarter(_:))*