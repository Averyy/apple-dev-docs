# CFCharacterSetIsSupersetOfSet(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Reports whether or not a character set is a superset of another set.

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
func CFCharacterSetIsSupersetOfSet(_ theSet: CFCharacterSet!, _ theOtherset: CFCharacterSet!) -> Bool
```

```c
extern Boolean CFCharacterSetIsSupersetOfSet(CFCharacterSetRef theSet, CFCharacterSetRef theOtherset);
```

#### Return Value

`true` if `theSet` is a superset of `theOtherSet`, otherwise `false`.

## Parameters

- `theSet`: The character set to be checked for the membership of `theOtherSet`.
- `theOtherset`: The character set to be checked whether or not it is a subset of `theSet`.

## See Also

### Querying Character Sets
- [func CFCharacterSetCreateBitmapRepresentation(CFAllocator!, CFCharacterSet!) -> CFData!](./cfcharactersetcreatebitmaprepresentation%28_,_%29.md)
  Creates a new immutable data with the bitmap representation from the given character set.
- [func CFCharacterSetHasMemberInPlane(CFCharacterSet!, CFIndex) -> Bool](./cfcharactersethasmemberinplane%28_,_%29.md)
  Reports whether or not a character set contains at least one member character in the specified plane.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](./cfcharactersetischaractermember%28_,_%29.md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsLongCharacterMember(CFCharacterSet!, UTF32Char) -> Bool](./cfcharactersetislongcharactermember%28_,_%29.md)
  Reports whether or not a given UTF-32 character is in a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetissupersetofset(_:_:))*