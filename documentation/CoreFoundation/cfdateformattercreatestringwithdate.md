# CFDateFormatterCreateStringWithDate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a string representation of the given date using the specified date formatter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDateFormatterCreateStringWithDate(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ date: CFDate!) -> CFString!
```

#### Return Value

A new string that represents `date` in the specified format. Returns `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `formatter`: The date formatter object that specifies the format of the returned string.
- `date`: The date object for which to create a string representation.

## See Also

- [func CFDateFormatterCreateStringWithAbsoluteTime(CFAllocator!, CFDateFormatter!, CFAbsoluteTime) -> CFString!](cfdateformattercreatestringwithabsolutetime(_:_:_:).md)
  Returns a string representation of the given absolute time using the specified date formatter.
- [func CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!](cfdateformattercreatedateformatfromtemplate(_:_:_:_:).md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreatestringwithdate(_:_:_:))*