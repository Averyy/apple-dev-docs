# CFCharacterSetCreateWithBitmapRepresentation(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new immutable character set with the bitmap representation specified by given data.

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
func CFCharacterSetCreateWithBitmapRepresentation(_ alloc: CFAllocator!, _ theData: CFData!) -> CFCharacterSet!
```

#### Return Value

A new character set containing the indicated characters from `theData`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theData`: If the data contains a Plane index byte outside of the valid Plane range (1 to 16), the behavior is undefined.

## See Also

- [func CFCharacterSetCreateCopy(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreatecopy(_:_:).md)
  Creates a new character set with the values from a given character set.
- [func CFCharacterSetCreateInvertedSet(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreateinvertedset(_:_:).md)
  Creates a new immutable character set that is the invert of the specified character set.
- [func CFCharacterSetCreateWithCharactersInRange(CFAllocator!, CFRange) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinrange(_:_:).md)
  Creates a new character set with the values from the given range of Unicode characters.
- [func CFCharacterSetCreateWithCharactersInString(CFAllocator!, CFString!) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinstring(_:_:).md)
  Creates a new character set with the values in the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatewithbitmaprepresentation(_:_:))*