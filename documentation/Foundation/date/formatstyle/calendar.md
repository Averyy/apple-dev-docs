# calendar

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The calendar to use when formatting the date.

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
var calendar: Calendar
```

#### Discussion

Defaults to [`autoupdatingCurrent`](../../nscalendar/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using `autoupdatingCurrent`.

## See Also

### Modifying a Date Format Style
- [func locale(Locale) -> Date.FormatStyle](./locale%28_%29.md)
  Modifies the date format style to use the specified locale.
- [var timeZone: TimeZone](./timezone.md)
  The time zone to use when formatting the date and time components.
- [var capitalizationContext: FormatStyleCapitalizationContext](./capitalizationcontext.md)
  The capitalization context to use when formatting the date.
- [var locale: Locale](./locale.md)
  The locale to use when formatting the date and time components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/calendar)*