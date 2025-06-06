# calendar

**Framework**: UIKit  
**Kind**: property

The calendar that the calendar view illustrates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var calendar: Calendar { get set }
```

#### Discussion

Defaults to [`current`](https://developer.apple.com/documentation/foundation/nscalendar/1408501-current), which is the user’s current calendar set in Settings.

## See Also

- [var locale: Locale](uicalendarview/locale.md)
  The locale the calendar view uses for calendar conventions.
- [var timeZone: TimeZone?](uicalendarview/timezone.md)
  The time zone from the date the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/calendar)*