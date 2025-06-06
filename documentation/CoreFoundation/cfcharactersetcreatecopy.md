# CFCharacterSetCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new character set with the values from a given character set.

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
func CFCharacterSetCreateCopy(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFCharacterSet!
```

#### Return Value

A new character set that is a copy of `theSet`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function tries to compact the backing store where applicable.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theSet`: The character set to copy.

## See Also

- [func CFCharacterSetCreateInvertedSet(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreateinvertedset(_:_:).md)
  Creates a new immutable character set that is the invert of the specified character set.
- [func CFCharacterSetCreateWithCharactersInRange(CFAllocator!, CFRange) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinrange(_:_:).md)
  Creates a new character set with the values from the given range of Unicode characters.
- [func CFCharacterSetCreateWithCharactersInString(CFAllocator!, CFString!) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinstring(_:_:).md)
  Creates a new character set with the values in the given string.
- [func CFCharacterSetCreateWithBitmapRepresentation(CFAllocator!, CFData!) -> CFCharacterSet!](cfcharactersetcreatewithbitmaprepresentation(_:_:).md)
  Creates a new immutable character set with the bitmap representation specified by given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatecopy(_:_:))*