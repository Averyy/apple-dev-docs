# calendar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The calendar that the calendar view illustrates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var calendar: Calendar { get set }
```

```objc
@property (nonatomic, copy, nonnull) NSCalendar * calendar;
```

#### Discussion

Defaults to [`current`](../../Foundation/nscalendar/current.md), which is the user’s current calendar set in Settings.

## See Also

### Setting calendar details
- [var locale: Locale](./locale.md)
  The locale the calendar view uses for calendar conventions.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone from the date the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/calendar)*