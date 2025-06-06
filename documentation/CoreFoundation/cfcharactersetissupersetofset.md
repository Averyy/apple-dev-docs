# CFCharacterSetIsSupersetOfSet(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a character set is a superset of another set.

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
func CFCharacterSetIsSupersetOfSet(_ theSet: CFCharacterSet!, _ theOtherset: CFCharacterSet!) -> Bool
```

#### Return Value

`true` if `theSet` is a superset of `theOtherSet`, otherwise `false`.

## Parameters

- `theSet`: The character set to be checked for the membership of  .
- `theOtherset`: The character set to be checked whether or not it is a subset of  .

## See Also

- [func CFCharacterSetCreateBitmapRepresentation(CFAllocator!, CFCharacterSet!) -> CFData!](cfcharactersetcreatebitmaprepresentation(_:_:).md)
  Creates a new immutable data with the bitmap representation from the given character set.
- [func CFCharacterSetHasMemberInPlane(CFCharacterSet!, CFIndex) -> Bool](cfcharactersethasmemberinplane(_:_:).md)
  Reports whether or not a character set contains at least one member character in the specified plane.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](cfcharactersetischaractermember(_:_:).md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsLongCharacterMember(CFCharacterSet!, UTF32Char) -> Bool](cfcharactersetislongcharactermember(_:_:).md)
  Reports whether or not a given UTF-32 character is in a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetissupersetofset(_:_:))*