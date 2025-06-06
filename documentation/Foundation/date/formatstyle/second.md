# second(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the date format style to use the specified second format style.

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
func second(_ format: Date.FormatStyle.Symbol.Second = .defaultDigits) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified second style.

#### Discussion

Values of [`Date.FormatStyle.Symbol.Second`](date/formatstyle/symbol/second.md) are [`defaultDigits`](date/formatstyle/symbol/second/defaultdigits.md) and [`twoDigits`](date/formatstyle/symbol/second/twodigits.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Second`](date/formatstyle/symbol/second.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().second(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().second(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().second()) // 5
```

If you don’t provide a format, the [`defaultDigits`](date/formatstyle/symbol/second/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `format`: The second format style applied to the date format style.

## See Also

- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle](date/formatstyle/hour(_:).md)
  Modifies the date format style to use the specified hour format style.
- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle](date/formatstyle/minute(_:).md)
  Modifies the date format style to use the specified minute format style.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle](date/formatstyle/secondfraction(_:).md)
  Modifies the date format style to use the specified second fraction format style.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle](date/formatstyle/timezone(_:).md)
  Modifies the date format style to use the specified time zone format style.
- [Date.FormatStyle.TimeStyle](date/formatstyle/timestyle.md)
  Type that defines time styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/second(_:))*