# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting the date and time components.

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

#### Discussion

The default value is [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using `autoupdatingCurrent.`

## See Also

- [var timeZone: TimeZone](date/formatstyle/timezone.md)
  The time zone to use when formatting the date and time components.
- [var calendar: Calendar](date/formatstyle/calendar.md)
  The calendar to use when formatting the date.
- [var capitalizationContext: FormatStyleCapitalizationContext](date/formatstyle/capitalizationcontext.md)
  The capitalization context to use when formatting the date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/locale)*