# init(string:)

**Framework**: Foundation  
**Kind**: init

Returns a date object initialized with a date and time value specified by a given string in the international string representation format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
convenience init?(string description: String)
```

#### Return Value

An `NSDate` object initialized with a date and time value specified by `aString`.

## Parameters

- `description`: You must specify all fields of the format string, including the time zone offset, which must have a plus or minus sign prefix.

## See Also

- [var description: String](nsdate/description.md)
  A string representation of the date object.
- [class func date(withNaturalLanguageString: String) -> Any?](nsdate/date(withnaturallanguagestring:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](nsdate/date(withnaturallanguagestring:locale:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](nsdate/date(with:).md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [func addTimeInterval(TimeInterval) -> Any](nsdate/addtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](nsdate/date(withcalendarformat:timezone:).md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](nsdate/description(withcalendarformat:timezone:locale:).md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(string:))*