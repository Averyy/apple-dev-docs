# addTimeInterval(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new date object that is set to a given number of seconds relative to the receiver.

**Availability**:
- iOS 2.0+ - Deprecated in 4.0
- iPadOS 2.0+ - Deprecated in 4.0
- Mac Catalyst 2.0+ - Deprecated in 4.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`addingTimeInterval(_:)`](./addingtimeinterval%28_%29.md) instead.

## Declaration

```swift
func addTimeInterval(_ seconds: TimeInterval) -> Any
```

```objc
- (id) addTimeInterval:(NSTimeInterval) seconds;
```

## Return Value

A new [`NSDate`](../nsdate.md) object that is set to `seconds` seconds relative to the receiver. The date returned might have a representation different from the receiver’s.

## Parameters

- `seconds`: The number of seconds to add to the receiver. Use a negative value for seconds to have the returned object specify a date before the receiver.

## See Also

### Related Documentation
- [func addingTimeInterval(TimeInterval) -> Self](./addingtimeinterval%28_%29.md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func timeIntervalSince(Date) -> TimeInterval](./timeintervalsince%28_%29.md)
  Returns the interval between the receiver and another given date.
### Legacy Operations
- [class func date(withNaturalLanguageString: String) -> Any?](./date%28withnaturallanguagestring%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](./date%28withnaturallanguagestring,locale%29.md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](./date%28with%29.md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](./init%28string%29.md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](./date%28withcalendarformat,timezone%29.md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](./description%28withcalendarformat,timezone,locale%29.md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/addtimeinterval(_:))*