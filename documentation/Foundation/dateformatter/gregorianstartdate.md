# gregorianStartDate

**Framework**: Foundation  
**Kind**: property

The start date of the Gregorian calendar for the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var gregorianStartDate: Date? { get set }
```

#### Discussion

This is used to specify the start date for the Gregorian calendar switch from the Julian calendar. Different locales switched at different times. Normally you should just accept the locale’s default date for the switch.

See [`NSCalendar`](nscalendar.md) for more information.

## See Also

- [var calendar: Calendar!](dateformatter/calendar.md)
  The calendar for the receiver.
- [var defaultDate: Date?](dateformatter/defaultdate.md)
  The default date for the receiver.
- [var locale: Locale!](dateformatter/locale.md)
  The locale for the receiver.
- [var timeZone: TimeZone!](dateformatter/timezone.md)
  The time zone for the receiver.
- [var twoDigitStartDate: Date?](dateformatter/twodigitstartdate.md)
  The earliest date that can be denoted by a two-digit year specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/gregorianstartdate)*