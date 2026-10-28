# date(withCalendarFormat:timeZone:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Converts the receiver to a calendar date with a given format string and time zone.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

> **Deprecated**: Use [`NSDate`](../nsdate.md) methods to set the individual date values.

## Declaration

```swift
func date(withCalendarFormat format: String?, timeZone aTimeZone: TimeZone?) -> NSCalendarDate
```

```objc
- (NSCalendarDate *) dateWithCalendarFormat:(NSString *) format timeZone:(NSTimeZone *) aTimeZone;
```

## Return Value

A new [`NSCalendarDate`](../nscalendardate.md) object bound to `format` and the time zone `aTimeZone`.

## Parameters

- `format`: The format for the returned string (see Date and Number Formatters in OS X v10.0 to 10.3 for a discussion of how to create the format string). Pass `nil` to use the default format string, “`%Y-%m-%d %H:%M:%S %z`” (this conforms to the international format `YYYY-MM-DD HH:MM:SS ±HHMM`.)
- `aTimeZone`: The time zone for the new calendar date. Pass `nil` to use the default time zone—specific to the current locale.

## See Also

### Legacy Operations
- [class func date(withNaturalLanguageString: String) -> Any?](./date%28withnaturallanguagestring%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](./date%28withnaturallanguagestring,locale%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](./date%28with%29.md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](./init%28string%29.md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func addTimeInterval(TimeInterval) -> Any](./addtimeinterval%28_%29.md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](./description%28withcalendarformat,timezone,locale%29.md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/date(withcalendarformat:timezone:))*