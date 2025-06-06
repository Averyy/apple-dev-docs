# CFAttributedStringCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an attributed string with specified string and attributes.

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
func CFAttributedStringCreate(_ alloc: CFAllocator!, _ str: CFString!, _ attributes: CFDictionary!) -> CFAttributedString!
```

#### Return Value

An attributed string that contains the characters from `str` and the attributes specified by `attributes`. The result is `NULL` if there was a problem in creating the attributed string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note that both the string and the attributes dictionary are copied. The specified attributes are applied to the whole string. If you want to apply different attributes to different ranges of the string, you should use a mutable attributed string.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new attributed string. Pass   or   to use the current default allocator.
- `str`: A string that specifies the characters to use in the new attributed string. This value is copied.
- `attributes`: A dictionary that contains the attributes to apply to the new attributed string. This value is copied.

## See Also

- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](cfattributedstringcreatecopy(_:_:).md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](cfattributedstringcreatewithsubstring(_:_:_:).md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](cfattributedstringgetlength(_:).md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](cfattributedstringgetstring(_:).md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreate(_:_:_:))*