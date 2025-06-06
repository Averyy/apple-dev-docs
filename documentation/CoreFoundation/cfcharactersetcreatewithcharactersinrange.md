# CFCharacterSetCreateWithCharactersInRange(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new character set with the values from the given range of Unicode characters.

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
func CFCharacterSetCreateWithCharactersInRange(_ alloc: CFAllocator!, _ theRange: CFRange) -> CFCharacterSet!
```

#### Return Value

A new character set that contains a contiguous range of Unicode characters. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theRange`: The Unicode range of characters of the new character set. The function accepts the range in 32-bit in the UTF-32 format. The valid character point range is from 0x00000 to 0x10FFFF.

## See Also

- [func CFCharacterSetCreateCopy(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreatecopy(_:_:).md)
  Creates a new character set with the values from a given character set.
- [func CFCharacterSetCreateInvertedSet(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreateinvertedset(_:_:).md)
  Creates a new immutable character set that is the invert of the specified character set.
- [func CFCharacterSetCreateWithCharactersInString(CFAllocator!, CFString!) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinstring(_:_:).md)
  Creates a new character set with the values in the given string.
- [func CFCharacterSetCreateWithBitmapRepresentation(CFAllocator!, CFData!) -> CFCharacterSet!](cfcharactersetcreatewithbitmaprepresentation(_:_:).md)
  Creates a new immutable character set with the bitmap representation specified by given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatewithcharactersinrange(_:_:))*