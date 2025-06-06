# date(with:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
class func date(with aString: String) -> Any
```

#### Return Value

An `NSDate` object with a date and time value specified by `aString`.

#### Discussion

To create a date object from a string, you should typically use a date formatter object instead (see [`DateFormatter`](dateformatter.md) and [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

## Parameters

- `aString`: You must specify all fields of the format string, including the time zone offset, which must have a plus or minus sign prefix.

## See Also

- [class func date(withNaturalLanguageString: String) -> Any?](nsdate/date(withnaturallanguagestring:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](nsdate/date(withnaturallanguagestring:locale:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [convenience init?(string: String)](nsdate/init(string:).md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func addTimeInterval(TimeInterval) -> Any](nsdate/addtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](nsdate/date(withcalendarformat:timezone:).md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](nsdate/description(withcalendarformat:timezone:locale:).md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/date(with:))*