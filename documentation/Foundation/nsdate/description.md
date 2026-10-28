# description

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string representation of the date object.

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
var description: String { get }
```

```objc
@property (copy, readonly) NSString * description;
```

## Discussion

The representation is useful for debugging only.

There are a number of options to acquire a formatted string for a date including: date formatters (see [`DateFormatter`](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)), and the `NSDate` methods [`description(with:)`](./description%28with%29.md), [`date(withCalendarFormat:timeZone:)`](./date%28withcalendarformat,timezone%29.md), and [`description(withCalendarFormat:timeZone:locale:)`](./description%28withcalendarformat,timezone,locale%29.md)

## See Also

### Related Documentation
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](./description%28withcalendarformat,timezone,locale%29.md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](./date%28withcalendarformat,timezone%29.md)
  Converts the receiver to a calendar date with a given format string and time zone.
### Describing Dates
- [func description(with: Any?) -> String](./description%28with%29.md)
  Returns a string representation of the date using the given locale.
- [var customPlaygroundQuickLook: PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/description)*