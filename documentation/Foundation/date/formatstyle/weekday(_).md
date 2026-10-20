# weekday(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the date format style to use the specified weekday format style.

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
func weekday(_ format: Date.FormatStyle.Symbol.Weekday = .abbreviated) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified week format style.

#### Discussion

Possible values of [`Date.FormatStyle.Symbol.Weekday`](date/formatstyle/symbol/weekday.md) include [`abbreviated`](date/formatstyle/symbol/weekday/abbreviated.md), [`narrow`](date/formatstyle/symbol/weekday/narrow.md), [`oneDigit`](date/formatstyle/symbol/weekday/onedigit.md), [`short`](date/formatstyle/symbol/weekday/short.md), [`twoDigits`](date/formatstyle/symbol/weekday/twodigits.md), and [`wide`](date/formatstyle/symbol/weekday/wide.md).

## Parameters

- `format`: The weekday format style applied to the date format style.

## See Also

- [func day(Date.FormatStyle.Symbol.Day) -> Date.FormatStyle](date/formatstyle/day(_:).md)
  Modifies the date format style to use the specified day format style.
- [func dayOfYear(Date.FormatStyle.Symbol.DayOfYear) -> Date.FormatStyle](date/formatstyle/dayofyear(_:).md)
  Modifies the date format style to use the specified day of the year format style.
- [func era(Date.FormatStyle.Symbol.Era) -> Date.FormatStyle](date/formatstyle/era(_:).md)
  Modifies the date format style to use the specified era format style.
- [func month(Date.FormatStyle.Symbol.Month) -> Date.FormatStyle](date/formatstyle/month(_:).md)
  Modifies the date format style to use the specified month format style.
- [func quarter(Date.FormatStyle.Symbol.Quarter) -> Date.FormatStyle](date/formatstyle/quarter(_:).md)
  Modifies the date format style to use the specified quarter format style.
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](date/formatstyle/week(_:).md)
  Modifies the date format style to use the specified week format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](date/formatstyle/year(_:).md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](date/formatstyle/datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/weekday(_:))*