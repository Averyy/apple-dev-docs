# timeZone(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified time zone format style.

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
func timeZone(_ format: Date.FormatStyle.Symbol.TimeZone = .specificName(.short)) -> Date.FormatStyle
```

#### Return Value

A date format style modified to include the specified time zone format style.

#### Discussion

Values of [`Date.FormatStyle.Symbol.TimeZone`](./symbol/timezone.md) are [`exemplarLocation`](./symbol/timezone/exemplarlocation.md) and [`genericLocation`](./symbol/timezone/genericlocation.md).

Static methods that return [`Date.FormatStyle.Symbol.TimeZone`](./symbol/timezone.md) objects include [`genericName(_:)`](./symbol/timezone/genericname%28_%29.md), [`identifier(_:)`](./symbol/timezone/identifier%28_%29.md),  [`iso8601(_:)`](./symbol/timezone/iso8601%28_%29.md), [`localizedGMT(_:)`](./symbol/timezone/localizedgmt%28_%29.md), and [`specificName(_:)`](./symbol/timezone/specificname%28_%29.md).

## Parameters

- `format`: The time zone format style applied to the date format style.

## See Also

### Specifying the Time Format
- [func hour(Date.FormatStyle.Symbol.Hour) -> Date.FormatStyle](./hour%28_%29.md)
  Modifies the date format style to use the specified hour format style.
- [func minute(Date.FormatStyle.Symbol.Minute) -> Date.FormatStyle](./minute%28_%29.md)
  Modifies the date format style to use the specified minute format style.
- [func second(Date.FormatStyle.Symbol.Second) -> Date.FormatStyle](./second%28_%29.md)
  Modifies the date format style to use the specified second format style.
- [func secondFraction(Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle](./secondfraction%28_%29.md)
  Modifies the date format style to use the specified second fraction format style.
- [Date.FormatStyle.TimeStyle](./timestyle.md)
  Type that defines time styles varied in length or components included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/timezone(_:))*