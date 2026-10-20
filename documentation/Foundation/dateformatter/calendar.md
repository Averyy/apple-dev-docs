# calendar

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The calendar for the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var calendar: Calendar! { get set }
```

```objc
@property (copy, null_resettable) NSCalendar * calendar;
```

#### Discussion

If unspecified, the logical calendar for the current user is used.

## See Also

### Managing Attributes
- [var defaultDate: Date?](./defaultdate.md)
  The default date for the receiver.
- [var locale: Locale!](./locale.md)
  The locale for the receiver.
- [var timeZone: TimeZone!](./timezone.md)
  The time zone for the receiver.
- [var twoDigitStartDate: Date?](./twodigitstartdate.md)
  The earliest date that can be denoted by a two-digit year specifier.
- [var gregorianStartDate: Date?](./gregorianstartdate.md)
  The start date of the Gregorian calendar for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/calendar)*