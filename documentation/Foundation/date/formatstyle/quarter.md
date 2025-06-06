# quarter(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A date format style modified to include the specified quarter style.

#### Discussion

Possible values of [`Date.FormatStyle.Symbol.Quarter`](date/formatstyle/symbol/quarter.md) include [`abbreviated`](date/formatstyle/symbol/quarter/abbreviated.md), [`narrow`](date/formatstyle/symbol/quarter/narrow.md), [`oneDigit`](date/formatstyle/symbol/quarter/onedigit.md), [`twoDigits`](date/formatstyle/symbol/month/twodigits.md), and [`wide`](date/formatstyle/symbol/month/wide.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Quarter`](date/formatstyle/symbol/quarter.md) format styles applied to a date:

```swift
let meetingDate = Date() // Oct 7, 2020 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().quarter(.abbreviated)) // Q4
meetingDate.formatted(Date.FormatStyle().quarter(.narrow)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter(.oneDigit)) // 4
meetingDate.formatted(Date.FormatStyle().quarter(.twoDigits)) // 04
meetingDate.formatted(Date.FormatStyle().quarter(.wide)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter()) // Q4

```

If you don’t provide a format, the [`abbreviated`](date/formatstyle/symbol/quarter/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `format`: The quarter format style applied to the date format style.

## See Also

- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle](date/formatstyle/day(_:).md)
  Modifies the date format style to use the specified day format style.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle](date/formatstyle/dayofyear(_:).md)
  Modifies the date format style to use the specified day of the year format style.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle](date/formatstyle/era(_:).md)
  Modifies the date format style to use the specified era format style.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle](date/formatstyle/month(_:).md)
  Modifies the date format style to use the specified month format style.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](date/formatstyle/week(_:).md)
  Modifies the date format style to use the specified week format style.
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](date/formatstyle/weekday(_:).md)
  Modifies the date format style to use the specified weekday format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](date/formatstyle/year(_:).md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](date/formatstyle/datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/quarter(_:))*