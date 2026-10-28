# locale

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The locale the calendar view uses for calendar conventions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var locale: Locale { get set }
```

```objc
@property (nonatomic, strong, nonnull) NSLocale * locale;
```

## Discussion

Defaults to [`current`](../../Foundation/nslocale/current.md).

## See Also

### Setting calendar details
- [var calendar: Calendar](./calendar.md)
  The calendar that the calendar view illustrates.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone from the date the calendar view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarview/locale)*