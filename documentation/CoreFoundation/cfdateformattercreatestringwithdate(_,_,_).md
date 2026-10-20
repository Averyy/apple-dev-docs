# CFDateFormatterCreateStringWithDate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a string representation of the given date using the specified date formatter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDateFormatterCreateStringWithDate(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ date: CFDate!) -> CFString!
```

```c
extern CFStringRefCFDateFormatterCreateStringWithDate(CFAllocatorRef allocator, CFDateFormatterRef formatter, CFDateRef date);
```

#### Return Value

A new string that represents `date` in the specified format. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `formatter`: The date formatter object that specifies the format of the returned string.
- `date`: The date object for which to create a string representation.

## See Also

### Creating Strings From Data
- [func CFDateFormatterCreateStringWithAbsoluteTime(CFAllocator!, CFDateFormatter!, CFAbsoluteTime) -> CFString!](./cfdateformattercreatestringwithabsolutetime%28_,_,_%29.md)
  Returns a string representation of the given absolute time using the specified date formatter.
- [func CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!](./cfdateformattercreatedateformatfromtemplate%28_,_,_,_%29.md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreatestringwithdate(_:_:_:))*