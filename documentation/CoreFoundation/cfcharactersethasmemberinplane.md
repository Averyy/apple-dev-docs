# CFCharacterSetHasMemberInPlane(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Reports whether or not a character set contains at least one member character in the specified plane.

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
func CFCharacterSetHasMemberInPlane(_ theSet: CFCharacterSet!, _ thePlane: CFIndex) -> Bool
```

#### Return Value

`true` if at least one member character is in the specified plane, otherwise `false`.

## Parameters

- `theSet`: The character set to examine.
- `thePlane`: The plane number to be checked for the membership. The valid value range is from 0 to 16. If the value is outside of the valid plane number range, the behavior is undefined.

## See Also

- [func CFCharacterSetCreateBitmapRepresentation(CFAllocator!, CFCharacterSet!) -> CFData!](cfcharactersetcreatebitmaprepresentation(_:_:).md)
  Creates a new immutable data with the bitmap representation from the given character set.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](cfcharactersetischaractermember(_:_:).md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsLongCharacterMember(CFCharacterSet!, UTF32Char) -> Bool](cfcharactersetislongcharactermember(_:_:).md)
  Reports whether or not a given UTF-32 character is in a character set.
- [func CFCharacterSetIsSupersetOfSet(CFCharacterSet!, CFCharacterSet!) -> Bool](cfcharactersetissupersetofset(_:_:).md)
  Reports whether or not a character set is a superset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersethasmemberinplane(_:_:))*