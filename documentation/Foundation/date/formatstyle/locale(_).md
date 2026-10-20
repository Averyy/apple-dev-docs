# locale(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date format style to use the specified locale.

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
func locale(_ locale: Locale) -> Date.FormatStyle
```

#### Return Value

A date format style with the provided locale.

## Parameters

- `locale`: The locale to use when formatting a date.

## See Also

### Modifying a Date Format Style
- [var timeZone: TimeZone](./timezone.md)
  The time zone to use when formatting the date and time components.
- [var calendar: Calendar](./calendar.md)
  The calendar to use when formatting the date.
- [var capitalizationContext: FormatStyleCapitalizationContext](./capitalizationcontext.md)
  The capitalization context to use when formatting the date.
- [var locale: Locale](./locale.md)
  The locale to use when formatting the date and time components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/locale(_:))*