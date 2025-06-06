# CFAttributedStringCreateMutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a mutable attributed string.

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
func CFAttributedStringCreateMutable(_ alloc: CFAllocator!, _ maxLength: CFIndex) -> CFMutableAttributedString!
```

#### Return Value

A new mutable attributed string. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: An allocator to be used to allocate memory for the new attributed string. Pass   or kCFAllocatorDefault to use the current default allocator.
- `maxLength`: Pass   to specify that the maximum length is not limited. The value must not be negative.

## See Also

- [func CFAttributedStringCreateMutableCopy(CFAllocator!, CFIndex, CFAttributedString!) -> CFMutableAttributedString!](cfattributedstringcreatemutablecopy(_:_:_:).md)
  Creates a mutable copy of an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatemutable(_:_:))*