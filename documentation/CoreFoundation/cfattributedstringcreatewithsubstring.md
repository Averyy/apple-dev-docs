# CFAttributedStringCreateWithSubstring(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a sub-attributed string from the specified range.

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
func CFAttributedStringCreateWithSubstring(_ alloc: CFAllocator!, _ aStr: CFAttributedString!, _ range: CFRange) -> CFAttributedString!
```

#### Return Value

A new attributed string whose string and attributes are copied from the specified range of the supplied attributed string. Returns `NULL` if there was a problem copying the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new attributed string. Pass   or   to use the current default allocator.
- `aStr`: The attributed string to copy.
- `range`: The range of the attributed string to copy.   must not exceed the bounds of  .

## See Also

- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](cfattributedstringcreate(_:_:_:).md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](cfattributedstringcreatecopy(_:_:).md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](cfattributedstringgetlength(_:).md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](cfattributedstringgetstring(_:).md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatewithsubstring(_:_:_:))*