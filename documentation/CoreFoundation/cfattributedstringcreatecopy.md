# CFAttributedStringCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable copy of an attributed string.

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
func CFAttributedStringCreateCopy(_ alloc: CFAllocator!, _ aStr: CFAttributedString!) -> CFAttributedString!
```

#### Return Value

An immutable attributed string with characters and attributes identical to those of `aStr`. Returns `NULL` if there was a problem copying the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new attributed string. Pass   or   to use the current default allocator.
- `aStr`: The attributed string to copy.

## See Also

- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](cfattributedstringcreate(_:_:_:).md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](cfattributedstringcreatewithsubstring(_:_:_:).md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](cfattributedstringgetlength(_:).md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](cfattributedstringgetstring(_:).md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatecopy(_:_:))*