# minute(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified minute format style.

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
func minute(_ format: Date.FormatStyle.Symbol.Minute = .defaultDigits) -> Date.FormatStyle
```

## Return Value

A date format style modified to include the specified minute style.

## Discussion

Values of [`Date.FormatStyle.Symbol.Minute`](./symbol/minute.md) are [`defaultDigits`](./symbol/minute/defaultdigits.md) and [`twoDigits`](./symbol/minute/twodigits.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Minute`](./symbol/minute.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().minute(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().minute(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().minute()) // 5
```

If you don’t provide a format, the [`defaultDigits`](./symbol/minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](../formatstyle.md).

## Parameters

- `format`: The minute format style applied to the date format style.

## See Also

### Specifying the Time Format
- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle](./hour%28_%29.md)
  Modifies the date format style to use the specified hour format style.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle](./second%28_%29.md)
  Modifies the date format style to use the specified second format style.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle](./secondfraction%28_%29.md)
  Modifies the date format style to use the specified second fraction format style.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle](./timezone%28_%29.md)
  Modifies the date format style to use the specified time zone format style.
- [Date.FormatStyle.TimeStyle](./timestyle.md)
  Type that defines time styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/minute(_:))*