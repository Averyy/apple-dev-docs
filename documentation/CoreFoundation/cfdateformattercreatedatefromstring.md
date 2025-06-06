# CFDateFormatterCreateDateFromString(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a date object representing a given string.

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
func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!) -> CFDate!
```

#### Return Value

A new date that represents `string`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `formatter`: The date formatter object to use to parse  .
- `string`: The string that contains the date.
- `rangep`: A reference to the range within the string specifying the substring to be parsed. If  , the whole string is parsed. Upon return, contains the range that defines the extent of the parse (may be less than the given range).

## See Also

- [func CFDateFormatterGetAbsoluteTimeFromString(CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool](cfdateformattergetabsolutetimefromstring(_:_:_:_:).md)
  Returns an absolute time object representing a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercreatedatefromstring(_:_:_:_:))*