# locale

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The locale for formatting the date and time interval components.

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
var locale: Locale
```

## Discussion

The default value is [`autoupdatingCurrent`](../../nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to use `autoupdatingCurrent.`

## See Also

### Specifying Date Interval Format Styles
- [func timeZone(Date.IntervalFormatStyle.Symbol.TimeZone) -> Date.IntervalFormatStyle](./timezone%28_%29.md)
  Modifies the date interval format style to use the specified time zone format.
- [func locale(Locale) -> Date.IntervalFormatStyle](./locale%28_%29.md)
  Modifies the date interval format style to use the specified locale.
- [var calendar: Calendar](./calendar.md)
  The calendar for formatting the date interval.
- [var timeZone: TimeZone](./timezone.md)
  The time zone for formatting the date interval components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/locale)*