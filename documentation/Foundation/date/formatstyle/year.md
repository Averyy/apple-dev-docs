# year(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the date format style to use the specified year format style.

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
func year(_ format: Date.FormatStyle.Symbol.Year = .defaultDigits) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified year format style.

#### Discussion

Possible values of [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md) include [`twoDigits`](date/formatstyle/symbol/year/twodigits.md), [`padded(_:)`](date/formatstyle/symbol/year/padded(_:).md), [`relatedGregorian(minimumLength:)`](date/formatstyle/symbol/year/relatedgregorian(minimumlength:).md), and [`extended(minimumLength:)`](date/formatstyle/symbol/year/extended(minimumlength:).md).

This example shows a variety of [`Date.FormatStyle.Symbol.Year`](date/formatstyle/symbol/year.md) formats applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().year(.defaultDigits)) // 2021
meetingDate.formatted(Date.FormatStyle().year(.twoDigits)) // 21
meetingDate.formatted(Date.FormatStyle().year(.padded(6))) // 002021
```

If you don’t provide a format, the [`defaultDigits`](date/formatstyle/symbol/day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `format`: The year format style applied to the date format style.

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
- [func weekday(Date.FormatStyle.Symbol.Weekday) -> Date.FormatStyle](date/formatstyle/weekday(_:).md)
  Modifies the date format style to use the specified weekday format style.
- [Date.FormatStyle.DateStyle](date/formatstyle/datestyle.md)
  Type that defines date styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/year(_:))*