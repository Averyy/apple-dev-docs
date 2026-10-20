# CFAttributedStringCreateWithSubstring(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a sub-attributed string from the specified range.

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
func CFAttributedStringCreateWithSubstring(_ alloc: CFAllocator!, _ aStr: CFAttributedString!, _ range: CFRange) -> CFAttributedString!
```

```c
extern CFAttributedStringRefCFAttributedStringCreateWithSubstring(CFAllocatorRef alloc, CFAttributedStringRef aStr, CFRange range);
```

#### Return Value

A new attributed string whose string and attributes are copied from the specified range of the supplied attributed string. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new attributed string. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `aStr`: The attributed string to copy.
- `range`: The range of the attributed string to copy. `range` must not exceed the bounds of `aStr`.

## See Also

### Creating a CFAttributedString
- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](./cfattributedstringcreate%28_,_,_%29.md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](./cfattributedstringcreatecopy%28_,_%29.md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](./cfattributedstringgetlength%28_%29.md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](./cfattributedstringgetstring%28_%29.md)
  Returns the string for an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatewithsubstring(_:_:_:))*