# date(withNaturalLanguageString:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a date object set to the date and time specified by a given string.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

> **Deprecated**: Create an NSDateFormatter with `init` and set the dateFormat property instead.

## Declaration

```swift
class func date(withNaturalLanguageString string: String) -> Any?
```

```objc
+ (id) dateWithNaturalLanguageString:(NSString *) string;
```

#### Return Value

A new `NSDate` object set to the current date and time specified by `string`.

#### Discussion

This method supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged. To create a date object from a string, you should use a date formatter object instead (see [`DateFormatter`](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

In parsing the string, this method uses the date and time preferences stored in the user’s defaults database. (See [`date(withNaturalLanguageString:locale:)`](./date%28withnaturallanguagestring,locale%29.md) for a list of the specific items used.)

## Parameters

- `string`: A string that contains a colloquial specification of a date, such as “last Tuesday at dinner,” “3pm December 31, 2001,” “12/31/01,” or “31/12/01.”

## See Also

### Legacy Operations
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](./date%28withnaturallanguagestring,locale%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](./date%28with%29.md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](./init%28string%29.md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func addTimeInterval(TimeInterval) -> Any](./addtimeinterval%28_%29.md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](./date%28withcalendarformat,timezone%29.md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](./description%28withcalendarformat,timezone,locale%29.md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/date(withnaturallanguagestring:))*