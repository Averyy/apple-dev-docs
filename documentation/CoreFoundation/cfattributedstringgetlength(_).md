# CFAttributedStringGetLength(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the length of the attributed string in characters.

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
func CFAttributedStringGetLength(_ aStr: CFAttributedString!) -> CFIndex
```

```c
extern CFIndex CFAttributedStringGetLength(CFAttributedStringRef aStr);
```

#### Return Value

The length of the attributed string in characters; this is the same as `CFStringGetLength(CFAttributedStringGetString(aStr))`.

## Parameters

- `aStr`: The attributed string to examine.

## See Also

### Creating a CFAttributedString
- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](./cfattributedstringcreate%28_,_,_%29.md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](./cfattributedstringcreatecopy%28_,_%29.md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](./cfattributedstringcreatewithsubstring%28_,_,_%29.md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](./cfattributedstringgetstring%28_%29.md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetlength(_:))*