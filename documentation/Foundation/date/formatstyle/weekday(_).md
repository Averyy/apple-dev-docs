# weekday(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

Possible values of [`Date.FormatStyle.Symbol.Weekday`](./symbol/weekday.md) include [`abbreviated`](./symbol/weekday/abbreviated.md), [`narrow`](./symbol/weekday/narrow.md), [`oneDigit`](./symbol/weekday/onedigit.md), [`short`](./symbol/weekday/short.md), [`twoDigits`](./symbol/weekday/twodigits.md), and [`wide`](./symbol/weekday/wide.md).

## Parameters

- `format`: The weekday format style applied to the date format style.

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
- [func week(Date.FormatStyle.Symbol.Week) -> Date.FormatStyle](./week%28_%29.md)
  Modifies the date format style to use the specified week format style.
- [func year(Date.FormatStyle.Symbol.Year) -> Date.FormatStyle](./year%28_%29.md)
  Modifies the date format style to use the specified year format style.
- [Date.FormatStyle.DateStyle](./datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/weekday(_:))*