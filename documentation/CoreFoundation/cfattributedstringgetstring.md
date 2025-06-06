# CFAttributedStringGetString(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the string for an attributed string.

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
func CFAttributedStringGetString(_ aStr: CFAttributedString!) -> CFString!
```

#### Return Value

An immutable string containing the characters from `aStr`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

For performance reasons, the string returned will often be the backing store of the attributed string, and it might therefore change if the attributed string is edited. However, this is an implementation detail, and you should not rely on this behavior.

## Parameters

- `aStr`: The attributed string to examine.

## See Also

- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](cfattributedstringcreate(_:_:_:).md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](cfattributedstringcreatecopy(_:_:).md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](cfattributedstringcreatewithsubstring(_:_:_:).md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](cfattributedstringgetlength(_:).md)
  Returns the length of the attributed string in characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstring(_:))*