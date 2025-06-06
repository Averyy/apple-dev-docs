# CFCharacterSetCreateBitmapRepresentation(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new immutable data with the bitmap representation from the given character set.

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
func CFCharacterSetCreateBitmapRepresentation(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFData!
```

#### Return Value

A new CFData object containing a bitmap representation of `theSet`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theSet`: The set from which to create a bitmap representation. Refer to the comments for   for the detailed discussion of the bitmap representation format.

## See Also

- [func CFCharacterSetHasMemberInPlane(CFCharacterSet!, CFIndex) -> Bool](cfcharactersethasmemberinplane(_:_:).md)
  Reports whether or not a character set contains at least one member character in the specified plane.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](cfcharactersetischaractermember(_:_:).md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsLongCharacterMember(CFCharacterSet!, UTF32Char) -> Bool](cfcharactersetislongcharactermember(_:_:).md)
  Reports whether or not a given UTF-32 character is in a character set.
- [func CFCharacterSetIsSupersetOfSet(CFCharacterSet!, CFCharacterSet!) -> Bool](cfcharactersetissupersetofset(_:_:).md)
  Reports whether or not a character set is a superset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatebitmaprepresentation(_:_:))*