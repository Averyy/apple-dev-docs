# CFDateFormatterCreateDateFormatFromTemplate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFDateFormatterCreateDateFormatFromTemplate(_ allocator: CFAllocator!, _ tmplate: CFString!, _ options: CFOptionFlags, _ locale: CFLocale!) -> CFString!
```

#### Return Value

A localized date format string representing the date format components given in `template`, arranged appropriately for the locale specified by `locale`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The returned string may not contain exactly those components given in `template`, but may—for example—have locale-specific adjustments applied.

#### Discussion

Different locales have different conventions for the ordering of date components. You use this method to get an appropriate format string for a given set of components for a specified locale (typically you use the current locale—see [`CFLocaleCopyCurrent()`](cflocalecopycurrent().md)).

The following example shows the difference between the date formats for British and American English:

```objc
CFStringRef dateComponents = CFSTR("yMMMMd");
 
CFLocaleRef usLocale = CFLocaleCreate(NULL, CFSTR("en_US"));
CFStringRef usDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, usLocale);
// Date format for English (United States): MMMM d, y
 
CFLocaleRef gbLocale = CFLocaleCreate(NULL, CFSTR("en_GB"));
CFStringRef gbDateFormatString =
    CFDateFormatterCreateDateFormatFromTemplate(NULL, dateComponents, 0, gbLocale);
// Date format for English (United Kingdom): d MMMM y
```

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `tmplate`: A string containing date format patterns (such as “MM” or “h”).   For full details, see  .
- `options`: No options are currently defined—pass  .
- `locale`: The locale for which the template is required.

## See Also

- [func CFDateFormatterCreateStringWithAbsoluteTime(CFAllocator!, CFDateFormatter!, CFAbsoluteTime) -> CFString!](cfdateformattercreatestringwithabsolutetime(_:_:_:).md)
  Returns a string representation of the given absolute time using the specified date formatter.
- [func CFDateFormatterCreateStringWithDate(CFAllocator!, CFDateFormatter!, CFDate!) -> CFString!](cfdateformattercreatestringwithdate(_:_:_:).md)
  Returns a string representation of the given date using the specified date formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreatedateformatfromtemplate(_:_:_:_:))*