# CFCharacterSetCreateWithCharactersInString(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new character set with the values in the given string.

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
func CFCharacterSetCreateWithCharactersInString(_ alloc: CFAllocator!, _ theString: CFString!) -> CFCharacterSet!
```

#### Return Value

A new character set containing the characters from `theString`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theString`: A string containing the characters for the new set.

## See Also

- [func CFCharacterSetCreateCopy(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreatecopy(_:_:).md)
  Creates a new character set with the values from a given character set.
- [func CFCharacterSetCreateInvertedSet(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreateinvertedset(_:_:).md)
  Creates a new immutable character set that is the invert of the specified character set.
- [func CFCharacterSetCreateWithCharactersInRange(CFAllocator!, CFRange) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinrange(_:_:).md)
  Creates a new character set with the values from the given range of Unicode characters.
- [func CFCharacterSetCreateWithBitmapRepresentation(CFAllocator!, CFData!) -> CFCharacterSet!](cfcharactersetcreatewithbitmaprepresentation(_:_:).md)
  Creates a new immutable character set with the bitmap representation specified by given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatewithcharactersinstring(_:_:))*