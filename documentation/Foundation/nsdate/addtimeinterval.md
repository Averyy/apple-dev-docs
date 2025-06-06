# addTimeInterval(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new date object that is set to a given number of seconds relative to the receiver.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addTimeInterval(_ seconds: TimeInterval) -> Any
```

#### Return Value

A new [`NSDate`](nsdate.md) object that is set to `seconds` seconds relative to the receiver. The date returned might have a representation different from the receiver’s.

## Parameters

- `seconds`: The number of seconds to add to the receiver. Use a negative value for seconds to have the returned object specify a date before the receiver.

## See Also

- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-71m1f.md)
  Returns a date object initialized relative to another given date by a given number of seconds.
- [func addingTimeInterval(TimeInterval) -> Self](nsdate/addingtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func timeIntervalSince(Date) -> TimeInterval](nsdate/timeintervalsince(_:).md)
  Returns the interval between the receiver and another given date.
- [class func date(withNaturalLanguageString: String) -> Any?](nsdate/date(withnaturallanguagestring:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](nsdate/date(withnaturallanguagestring:locale:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](nsdate/date(with:).md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](nsdate/init(string:).md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](nsdate/date(withcalendarformat:timezone:).md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](nsdate/description(withcalendarformat:timezone:locale:).md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/addtimeinterval(_:))*