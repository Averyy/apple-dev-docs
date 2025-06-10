# locale

**Framework**: UIKit  
**Kind**: property

The locale the calendar view uses for calendar conventions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var locale: Locale { get set }
```

#### Discussion

Defaults to [`current`](https://developer.apple.com/documentation/Foundation/NSLocale/current).

## See Also

- [var calendar: Calendar](uicalendarview/calendar.md)
  The calendar that the calendar view illustrates.
- [var timeZone: TimeZone?](uicalendarview/timezone.md)
  The time zone from the date the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/locale)*