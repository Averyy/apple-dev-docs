# description(withCalendarFormat:timeZone:locale:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string representation of the date formatted as specified by given conversion specifiers.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
func description(withCalendarFormat format: String?, timeZone aTimeZone: TimeZone?, locale: Any?) -> String?
```

```objc
- (NSString *) descriptionWithCalendarFormat:(NSString *) format timeZone:(NSTimeZone *) aTimeZone locale:(id) locale;
```

#### Return Value

A string representation of the receiver, formatted as specified by the given conversion specifiers.

#### Discussion

There are several problems with the implementation of this method that cannot be fixed for compatibility reasons. To format a date, you should use a date formatter object instead (see [`DateFormatter`](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

You could use this method to print the current time as follows:

```objc
sprintf(aString, "The current time is %s\n", [[[NSDate  date]
    descriptionWithCalendarFormat:@"%H:%M:%S %Z" timeZone:nil
    locale:[[NSUserDefaults standardUserDefaults] dictionaryRepresentation]]
        UTF8String]);
```

## Parameters

- `format`: The format for the returned string (see Date and Number Formatters in OS X v10.0 to 10.3 for a discussion of how to create the format string). Pass `nil` to use the default format string, “`%Y-%m-%d %H:%M:%S %z`” (this conforms to the international format `YYYY-MM-DD HH:MM:SS ±HHMM`.)
- `aTimeZone`: The time zone in which to represent the receiver. Pass `nil` to use the default time zone—specific to the current locale.
- `locale`: An `NSDictionary` object containing locale data. To use the user’s preferences, you can use `[[NSUserDefaults standardUserDefaults] dictionaryRepresentation]`.

  If you pass `nil` or an instance of `NSLocale`, `NSDate` uses the system default locale—this is not the same as the current user’s locale.

## See Also

### Related Documentation
- [func description(with: Any?) -> String](./description%28with%29.md)
  Returns a string representation of the date using the given locale.
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
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](./date%28withcalendarformat,timezone%29.md)
  Converts the receiver to a calendar date with a given format string and time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/description(withcalendarformat:timezone:locale:))*