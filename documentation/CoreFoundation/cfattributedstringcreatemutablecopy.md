# CFAttributedStringCreateMutableCopy(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a mutable copy of an attributed string.

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
func CFAttributedStringCreateMutableCopy(_ alloc: CFAllocator!, _ maxLength: CFIndex, _ aStr: CFAttributedString!) -> CFMutableAttributedString!
```

#### Return Value

A mutable copy of `aStr`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to be used to allocate memory for the new attributed string. Pass   or kCFAllocatorDefault to use the current default allocator.
- `maxLength`: Pass   to specify that the maximum length is not limited. If non- ,   must be greater than or equal to the length of  .
- `aStr`: The attributed string to copy.

## See Also

- [func CFAttributedStringCreateMutable(CFAllocator!, CFIndex) -> CFMutableAttributedString!](cfattributedstringcreatemutable(_:_:).md)
  Creates a mutable attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatemutablecopy(_:_:_:))*