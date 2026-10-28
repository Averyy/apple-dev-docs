# CFAttributedStringCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an immutable copy of an attributed string.

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
func CFAttributedStringCreateCopy(_ alloc: CFAllocator!, _ aStr: CFAttributedString!) -> CFAttributedString!
```

```c
extern CFAttributedStringRefCFAttributedStringCreateCopy(CFAllocatorRef alloc, CFAttributedStringRef aStr);
```

## Return Value

An immutable attributed string with characters and attributes identical to those of `aStr`. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new attributed string. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `aStr`: The attributed string to copy.

## See Also

### Creating a CFAttributedString
- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](./cfattributedstringcreate%28_,_,_%29.md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](./cfattributedstringcreatewithsubstring%28_,_,_%29.md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](./cfattributedstringgetlength%28_%29.md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](./cfattributedstringgetstring%28_%29.md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatecopy(_:_:))*