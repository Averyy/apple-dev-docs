# date(withNaturalLanguageString:locale:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a date object set to the date and time specified by a given string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
class func date(withNaturalLanguageString string: String, locale: Any?) -> Any?
```

#### Return Value

A new `NSDate` object set to the date and time specified by `string` as interpreted according to `locale`.

#### Discussion

This method supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged. To create a date object from a string, you should use a date formatter object instead (see [`DateFormatter`](dateformatter.md) and [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

The keys and values that represent the locale data from `locale` are used when parsing the string. In addition to the locale keys listed in the class description, these keys are used when parsing natural language strings:

- NSDateTimeOrdering
- NSEarlierTimeDesignations
- NSHourNameDesignations
- NSLaterTimeDesignations
- NSNextDayDesignations
- NSNextNextDayDesignations
- NSPriorDayDesignations
- NSThisDayDesignations
- NSYearMonthWeekDesignations

## Parameters

- `string`: A string that contains a colloquial specification of a date, such as “last Tuesday at dinner,” “3pm December 31, 2001,” “12/31/01,” or “31/12/01.”
- `locale`: If you pass   or an instance of  ,   uses the system default locale—this is not the same as the current user’s locale.

## See Also

- [class func date(withNaturalLanguageString: String) -> Any?](nsdate/date(withnaturallanguagestring:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](nsdate/date(with:).md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](nsdate/init(string:).md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func addTimeInterval(TimeInterval) -> Any](nsdate/addtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](nsdate/date(withcalendarformat:timezone:).md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](nsdate/description(withcalendarformat:timezone:locale:).md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/date(withnaturallanguagestring:locale:))*