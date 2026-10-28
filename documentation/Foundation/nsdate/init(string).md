# init(string:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a date object initialized with a date and time value specified by a given string in the international string representation format.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

> **Deprecated**: Use NSDateFormatter instead

## Declaration

```swift
convenience init?(string description: String)
```

```objc
- (id) initWithString:(NSString *) description;
```

## Return Value

An `NSDate` object initialized with a date and time value specified by `aString`.

## Parameters

- `description`: A string that specifies a date and time value in the international string representation format—`YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` is a time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”).

  You must specify all fields of the format string, including the time zone offset, which must have a plus or minus sign prefix.

## See Also

### Related Documentation
- [var description: String](./description.md)
  A string representation of the date object.
### Legacy Operations
- [class func date(withNaturalLanguageString: String) -> Any?](./date%28withnaturallanguagestring%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](./date%28withnaturallanguagestring,locale%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](./date%28with%29.md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [func addTimeInterval(TimeInterval) -> Any](./addtimeinterval%28_%29.md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](./date%28withcalendarformat,timezone%29.md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](./description%28withcalendarformat,timezone,locale%29.md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/init(string:))*