# CFCharacterSetCreateMutableCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new mutable character set with the values from another character set.

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
func CFCharacterSetCreateMutableCopy(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFMutableCharacterSet!
```

#### Return Value

A new mutable character set containing the same characters as `theSet`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theSet`: The character set to copy.

## See Also

- [func CFCharacterSetCreateMutable(CFAllocator!) -> CFMutableCharacterSet!](cfcharactersetcreatemutable(_:).md)
  Creates a new empty mutable character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatemutablecopy(_:_:))*