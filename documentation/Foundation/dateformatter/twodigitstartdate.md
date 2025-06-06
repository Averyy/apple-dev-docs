# twoDigitStartDate

**Framework**: Foundation  
**Kind**: property

The earliest date that can be denoted by a two-digit year specifier.

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
var twoDigitStartDate: Date? { get set }
```

#### Discussion

If the two-digit start date is set to January 6, 1976, then “January 1, 76” is interpreted as New Year’s Day in 2076, whereas “February 14, 76” is interpreted as Valentine’s Day in 1976.

By default, this property is equal to December 31, 1949.

## See Also

- [var calendar: Calendar!](dateformatter/calendar.md)
  The calendar for the receiver.
- [var defaultDate: Date?](dateformatter/defaultdate.md)
  The default date for the receiver.
- [var locale: Locale!](dateformatter/locale.md)
  The locale for the receiver.
- [var timeZone: TimeZone!](dateformatter/timezone.md)
  The time zone for the receiver.
- [var gregorianStartDate: Date?](dateformatter/gregorianstartdate.md)
  The start date of the Gregorian calendar for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/twodigitstartdate)*