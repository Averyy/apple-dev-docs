# hour(_:)

**Framework**: Foundation  
**Kind**: method

Modifies the date format style to use the specified hour format style.

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
func hour(_ format: Date.FormatStyle.Symbol.Hour = .defaultDigits(amPM: .abbreviated)) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified hour style.

#### Discussion

Values of [`Date.FormatStyle.Symbol.Hour`](date/formatstyle/symbol/hour.md) are [`defaultDigitsNoAMPM`](date/formatstyle/symbol/hour/defaultdigitsnoampm.md) and [`twoDigitsNoAMPM`](date/formatstyle/symbol/hour/twodigitsnoampm.md).

Static methods that return [`Date.FormatStyle.Symbol.Hour`](date/formatstyle/symbol/hour.md) objects include [`conversationalDefaultDigits(amPM:)`](date/formatstyle/symbol/hour/conversationaldefaultdigits(ampm:).md), [`conversationalTwoDigits(amPM:)`](date/formatstyle/symbol/hour/conversationaltwodigits(ampm:).md), [`defaultDigits(amPM:)`](date/formatstyle/symbol/hour/defaultdigits(ampm:).md), and [`twoDigitsNoAMPM`](date/formatstyle/symbol/hour/twodigitsnoampm.md).

This example shows a variety of [`Date.FormatStyle.Symbol.Hour`](date/formatstyle/symbol/hour.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM
meetingDate.formatted(Date.FormatStyle().hour(.defaultDigitsNoAMPM)) 
// 7

meetingDate.formatted(Date.FormatStyle().hour(.twoDigitsNoAMPM)) 
// 07

meetingDate.formatted(Date.FormatStyle().hour(.defaultDigits(amPM: .narrow))) 
// 7p

meetingDate.formatted(Date.FormatStyle().hour(.twoDigits(amPM: .abbreviated))
// 07 PM

meetingDate.formatted(Date.FormatStyle().hour(.conversationalDefaultDigits(amPM: .wide))
// 7 P.M.
```

If you don’t provide a format, the [`defaultDigits`](date/formatstyle/symbol/minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `format`: The hour format style applied to the date format style.

## See Also

- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle](date/formatstyle/minute(_:).md)
  Modifies the date format style to use the specified minute format style.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle](date/formatstyle/second(_:).md)
  Modifies the date format style to use the specified second format style.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle](date/formatstyle/secondfraction(_:).md)
  Modifies the date format style to use the specified second fraction format style.
- [func timeZone(Date.FormatStyle.Symbol.TimeZone) -> Date.FormatStyle](date/formatstyle/timezone(_:).md)
  Modifies the date format style to use the specified time zone format style.
- [Date.FormatStyle.TimeStyle](date/formatstyle/timestyle.md)
  Type that defines time styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/hour(_:))*