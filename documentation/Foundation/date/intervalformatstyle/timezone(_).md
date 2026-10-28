# timeZone(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date interval format style to use the specified time zone format.

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
func timeZone(_ format: Date.IntervalFormatStyle.Symbol.TimeZone = .genericName(.short)) -> Date.IntervalFormatStyle
```

## Return Value

A date interval format style with the provided time zone format.

## Parameters

- `format`: The time zone format style for formatting a date interval.

## See Also

### Specifying Date Interval Format Styles
- [func locale(Locale) -> Date.IntervalFormatStyle](./locale%28_%29.md)
  Modifies the date interval format style to use the specified locale.
- [var calendar: Calendar](./calendar.md)
  The calendar for formatting the date interval.
- [var locale: Locale](./locale.md)
  The locale for formatting the date and time interval components.
- [var timeZone: TimeZone](./timezone.md)
  The time zone for formatting the date interval components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/timezone(_:))*