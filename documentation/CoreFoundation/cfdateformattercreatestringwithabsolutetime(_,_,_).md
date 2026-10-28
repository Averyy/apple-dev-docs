# CFDateFormatterCreateStringWithAbsoluteTime(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a string representation of the given absolute time using the specified date formatter.

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
func CFDateFormatterCreateStringWithAbsoluteTime(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ at: CFAbsoluteTime) -> CFString!
```

```c
extern CFStringRefCFDateFormatterCreateStringWithAbsoluteTime(CFAllocatorRef allocator, CFDateFormatterRef formatter, CFAbsoluteTime at);
```

## Return Value

A new string that represents `at` in the specified format. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `formatter`: The date formatter object that specifies the format of the returned string.
- `at`: The absolute time for which to generate a string representation.

## See Also

### Creating Strings From Data
- [func CFDateFormatterCreateStringWithDate(CFAllocator!, CFDateFormatter!, CFDate!) -> CFString!](./cfdateformattercreatestringwithdate%28_,_,_%29.md)
  Returns a string representation of the given date using the specified date formatter.
- [func CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!](./cfdateformattercreatedateformatfromtemplate%28_,_,_,_%29.md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreatestringwithabsolutetime(_:_:_:))*