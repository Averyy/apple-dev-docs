# CFAttributedStringGetLength(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the length of the attributed string in characters.

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
func CFAttributedStringGetLength(_ aStr: CFAttributedString!) -> CFIndex
```

#### Return Value

The length of the attributed string in characters; this is the same as `CFStringGetLength(CFAttributedStringGetString(aStr))`.

## Parameters

- `aStr`: The attributed string to examine.

## See Also

- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](cfattributedstringcreate(_:_:_:).md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](cfattributedstringcreatecopy(_:_:).md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](cfattributedstringcreatewithsubstring(_:_:_:).md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](cfattributedstringgetstring(_:).md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetlength(_:))*